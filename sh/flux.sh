#!/bin/bash
PATH=/bin:/usr/bin:/sbin:/usr/sbin:/usr/local/lib

 case $1 in
   start)
         /usr/local/bin/xflux -l 40.90N -g 118.79E -k 3400
     ;;
   stop)
         kill -9 `pgrep xflux`
     ;;
   restart|reload)
         $0 stop
         sleep 3
         $0 start
     ;;
   status)
         exit 4
     ;;
   *)
     echo "Usage: $0 {start|stop|restart|reload|status}"
     exit 1
     ;;
 esac

 exit 0

