include("ʕ╯•ᴥ•ʔ╯︵‾‾.jl")

function mul(x, y)
    x * y
end

a = 7
b = 11

println(@ʕ╯•ᴥ•ʔ╯︵‾‾ mul_a_b)
println(@ʕ╯•ᴥ•ʔ╯︵‾‾ mul_3_4)

println(map((x -> @ʕ╯•ᴥ•ʔ╯︵‾‾ mul_x_a), [1,2,3,4]))
