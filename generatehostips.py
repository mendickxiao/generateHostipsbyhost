import socket
import sys
import getopt

def get_HostIps(host_name):
    hostips = []
    try:
       host_name = host_name.strip('\n')
       netinfo = socket.gethostbyname_ex(host_name)
       #print(netinfo)
       for ip in netinfo[2]:
           hostips.append("{0},{1}".format(host_name, ip))
    except:
       print("Unable to get HostIp, ", host_name)
    return hostips

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print("generatehostips.py -i <inputfile> -o <outputfile>")
        sys.exit(2)

    if not opts:
        print("generatehostips.py -i <inputfile> -o <outputfile>")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print("generatehostips.py -i <inputfile> -o <outputfile>")
        elif opt in ("-i", "--file"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    print("Input file is {0}, Output file is {1}".format(inputfile, outputfile))

    outputs = []
    with open(inputfile, 'r') as fp:
        for line in fp:
            outputs.extend(get_HostIps(line))

    with open(outputfile, 'w') as outfp:
        for output in outputs:
            outfp.write(output + '\n')

    print("finished the handle")

if __name__ == "__main__":
    main(sys.argv[1:])



