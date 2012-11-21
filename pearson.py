import sys, argparse

parser = argparse.ArgumentParser(description="ArgumentParser")
parser.add_argument('--target', required=True)
parser.add_argument('--input', action='append', required=True)
args = parser.parse_args()

feed_target = int(args.target)
feed_inputs = {}

x = 0
for i in sorted(args.input):
  feed_inputs[x] = int(i)
  x += 1

if len(feed_inputs.keys()) != 2:
  print "Need two valid input ingredients"
  sys.exit()

if (feed_inputs[0] < feed_target < feed_inputs[1]) == False:
  print "Target percentage must be between the two input ingredients"
  sys.exit()

ratio_0 = abs(feed_inputs[0] - feed_target)
ratio_1 = abs(feed_inputs[1] - feed_target)


print "Processing feed requirements for a target percentage of %d%%" % feed_target
print "Inputs:"
for i in feed_inputs:
  print "  Input %d is %d percent protein" % (i+1, feed_inputs[i])
print " "
print "You should use %d parts of ingredient 1 (%d%%) and %d parts of ingredient 2 (%d%%)" % (ratio_0, feed_inputs[0], ratio_1, feed_inputs[1])




