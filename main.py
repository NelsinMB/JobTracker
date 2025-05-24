import argparse
parser = argparse.ArgumentParser(prog="jobapp")

# ' dest='command' ': Tells asrgparse to store the name of the subcommmand used in the args namespace under the attribute args.command
subparsers = parser.add_subparsers(dest='command', required=True)


def handle_add(args):
    print("test")
    
def handle_list(args):
    return


add_parser = subparsers.add_parser('add', help='Add a new job application')
add_parser.add_argument('position')
add_parser.add_argument('company')
add_parser.add_argument('cv_path')
add_parser.set_defaults(func=handle_add)

list_parser = subparsers.add_parser('list', help='List all job applications')
# Add verbose version later.


#parser.add_argument("pos_name", type=str, help="The name of the position, ideally exactly as it is stated.")
#parser.add_argument("org_name", type=str, help="The name of the organization.")
#parser.add_argument("-t", "--test_opt", action="store_true") # Adding action makes it a flag. Note that because '--' is at the start of the first argument, it is an optional argument.

args = parser.parse_args()
args.func(args) # Call the function that handles the command entered, with the parameters entered.
print(args)