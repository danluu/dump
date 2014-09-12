include("peakflops_include.jl")

# fuzz.jl can easily hang/segfault julia, but we can't just replay the log
# since everything was run in a try/catch block to throw away exceptions

function rerun()
    f = open("log")
    line = readline(f)
    while line != ""
        try
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
