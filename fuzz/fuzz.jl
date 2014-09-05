const test_dir = "jl_input"

function generate_tests(n::Int)
    for i in 1:n
        len = rand(1:2^19-5000)
        f = open("$(test_dir)/$(i)","w")
        write(f, randstring(len))
        close(f)
    end
end

generate_tests(2^12)
