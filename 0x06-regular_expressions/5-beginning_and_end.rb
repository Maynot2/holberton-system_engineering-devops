#!/usr/bin/env ruby

if ARGV
	puts "#{ARGV[0]}".scan(/\Ah.n\z/).join
end
