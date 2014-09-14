# fuzz.jl can easily hang/segfault julia, but we can't just replay the log
# since everything was run in a try/catch block to throw away exceptions

function rerun()
    f = open("log")
    line = readline(f)
    i = 0
    while line != ""
        try
            i += 1
            if i & 0xffff == 0xffff
                print(".")
            end
            if line[1] == "#"
                continue
            end
            eval(parse(line))
        catch
        end
        line = readline(f)
    end
end

rerun()
