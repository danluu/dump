# peakflops often seems to cause a hang. What happens if we just try it a lot?

function wheee()
    i = 0
    while true
        try
            if i == 0
                print(".")
            end
            i += 1
            peakflops(1954784290346684782)
        catch
        end
    end
end


# print(code_typed(wheee, ()))
print(code_llvm(wheee, ()))
# wheee()
