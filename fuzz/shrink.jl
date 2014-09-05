const test_dir = "jl_input"

# Note that it takes a really long time for julia
# to construct a huge string. Seems like a super
# low priority performance bug to debug someday.
function generate_tests(n::Int, string::Bool)
    for i in 1:n
        len = 2^i
        f = open("$(test_dir)/$(i)","w")
        if string
            write(f,"\"")
        end
        write(f, randstring(len))
        if string
            write(f,"\"")
        end
        close(f)
    end
end

generate_tests(20, false)
