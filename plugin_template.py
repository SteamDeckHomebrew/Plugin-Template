class Plugin:
    # The name of the plugin. This string will be displayed in the Plugin menu
    name = "Template Plugin"
    # The name of the plugin author
    author = "Template Author"

    # If the plugin should be reloaded from a call to /plugins/reload or a file change
    hot_reload = False

    # The HTML that will be loaded when selecting the plugin in the list
    main_view_html = "<html><body><h2>Hello World</h2></body></html>"

    # The HTML that will be used to display a widget in the plugin main page
    tile_view_html = ""

    # A normal method. It can be called from JavaScript using call_plugin_function("method_1", argument1, argument2)
    async def method_1(self, *args):
        pass

    # A normal method. It can be called from JavaScript using call_plugin_function("method_2", argument1, argument2)
    async def method_2(self, *args):
        pass

    # Asyncio-compatible long-running code, executed in a task when the plugin is loaded
    async def __main(self):
        pass