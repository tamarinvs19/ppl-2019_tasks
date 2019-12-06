struct edge
    to::Int
    from::Int
    w::Int
end

function relax(e::edge)
    global d, p, x
    if d[e.to] > d[e.from] + e.w
	d[e.to] = d[e.from] + e.w
	p[e.to] = e.from
	x = e.to
    end
end

function ford()
    global es, d, p, n, x
    for i = 1:n
	for e in es
	    relax(e)
	end
    end
end


function read()
    n = parse(Int, readline())
    xs = 
end

