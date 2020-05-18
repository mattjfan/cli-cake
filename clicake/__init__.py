import sys
def runnable(_func = None, args = sys.argv[1:]):
    '''
        decorator for making scripts CLI callable.
        Returns a method that looks up CLI args and invokes
        function when called.
        Positional arguments are set just by listing the args in order,
        named arguments can be specified by using the flag with
        the same name as the arg prepended by -- (i.e. an arg called "file"
        could be set by `--file examplefilename.txt`)
    '''
    def _runnable(callback):
        def cast_arg(arg):
            def custom_cast(b):
                if b == 'True':
                    return True
                if b == 'False':
                    return False
                if b == 'None':
                    return None
                raise ValueError('Not Boolean')
            for cast in (custom_cast, int, float):
                try:
                    return cast(arg)
                except ValueError:
                    pass
            return arg
        def run_callback():
            # args = parser.parse_args()
            curr_arg='_args'
            parsed_args={'_args': []}
            curr_arg_values = []
            def update_args(new_curr_arg):
                nonlocal curr_arg
                nonlocal curr_arg_values
                if curr_arg == '_args':
                    pass
                elif len(curr_arg_values) == 0:
                    parsed_args[curr_arg] = True
                elif len(curr_arg_values) == 1:
                    parsed_args[curr_arg] = curr_arg_values[0]
                else:
                    parsed_args[curr_arg] = curr_arg_values
                curr_arg = new_curr_arg.strip('-')
                curr_arg_values = []
            for arg in args:
                if arg.startswith(('-','--')):
                    update_args(arg)
                else:
                    arg = cast_arg(arg)
                    if curr_arg == '_args':
                        parsed_args['_args'].append(arg)
                    else:
                        curr_arg_values.append(arg)
            update_args('')

            pargs = parsed_args['_args']
            del parsed_args['_args']
            callback(*pargs,**parsed_args)
        return run_callback
    if callable(_func): # If the first positional argument passed is a function,
        # then don't return decorator, just return decorated function
        # allows for decorator to be called like
        # @runnable
        # or 
        # @runnable() for when we want to pass in additional stuff
        return _runnable(_func)
    return _runnable

def run(callback, **kwargs):
    """
    Locally wraps the callback with a runnable() decorator
    and runs it. Can pass same optional args here as you can
    to runnable
    """
    return runnable(**kwargs)(callback)()