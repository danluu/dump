const test_dir = "jl_input"

# Find shortest too-long symbol bug.
function generate_tests(n::Int)
    for i in 1:n
        len = 2^i
        f = open("$(test_dir)/$(i)","w")
        write(f, randstring(len))
        close(f)
    end
end

# generate_tests(20)

# find shorter PCRE bug.
# This turned out to be a bug in pcregrep and not pcre itself.
function foo()
    prefix_len = rand(0:8000000)
    postfix_len = rand(0:80)
    text = "not defined"
    regex = r"not defined"
    dut = string(randstring(prefix_len),text,randstring(postfix_len))
    if !ismatch(regex, dut)
        print("ERROR: $dut")
    end
end

while true
    foo()
end
