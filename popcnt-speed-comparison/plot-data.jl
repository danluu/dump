using DataFrames
using Gadfly

df = readtable("data-1.csv")
for name in names(df)
    if name != :bytes
        df[name] = df[:bytes] ./ df[name]
    end
end
framed=melt(df,:bytes)
p = plot(framed, x=:bytes,y=:value,color=:variable,Geom.line)
draw(PNG("bytes_per_cycle-1.png",10inch,8inch),p)
