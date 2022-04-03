class Plugin:
    # The name of the plugin. This string will be displayed in the Plugin menu
    name = "Template Plugin"
    # The name of the plugin author
    author = "Template Author"

    # The HTML that will be loaded when selecting the plugin in the list
    main_view_html = "<html><body><h2>Hello World</h2></body></html>"
    # The HTML that will be used to display a widget in the plugin main page
    tile_view_html = ""

    # A private method. Any method that gets prefixed by a double underscore (__) will not be callable from JavaScript
    async def __private_method(*args):
        pass

    # A normal method. It can be called from JavaScript using call_plugin_function("method_1", argument1, argument2)
    async def method_1(*args):
        pass

    # A normal method. It can be called from JavaScript using call_plugin_function("method_2", argument1, argument2)
    async def method_2(*args):
        pass
