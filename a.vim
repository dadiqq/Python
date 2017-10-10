
://www.zhihu.com/question/19655689/answer/137028383
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

""""""""""""""""""""""
    "Quickly Run
    "    """"""""""""""""""""""
    map <F5> :call CompileRunGcc()<CR>
    func! CompileRunGcc()
        exec "w"
if &filetype == 'c'
            exec "!g++ % -o %<"
            exec "!time ./%<"
elseif &filetype == 'cpp'
            exec "!g++ % -o %<"
            exec "!time ./%<"
elseif &filetype == 'java'
            exec "!javac %"
            exec "!time java %<"
elseif &filetype == 'sh'
            :!time bash %
elseif &filetype == 'python'
            exec "!time python3 %"
elseif &filetype == 'html'
            exec "!firefox % &"
elseif &filetype == 'go'
    "        exec "!go build %<"
    "                    exec "!time go run %"
    "                    elseif &filetype == 'mkd'
    "                                exec "!~/.vim/markdown.pl % > %.html &"
    "                                            exec "!firefox %.html &"
    "                                            endif
    "                                                endfuncor if __name__ == '__main__':
