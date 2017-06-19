import os

from cursesmenu import *
from cursesmenu.items import *

from operations.folders.assertRules import AssertRules as FolderAssertRules
from operations.folders.setIcon import SetIcon as FolderSetIcon

from operations.files.rename import Rename as FileRename


def main():
    # Create the menu
    menu = CursesMenu("Python Folder Manager", "a Windows utility")
    menu_divider_folder = MenuItem("===FOLDER UTILITIES===")
    menu_function_set_icon = FunctionItem("Set .ico files as folder icons",
                                          FolderSetIcon.run(),
                                          ["Enter the desired root directory (current directory if empty):"])
    menu_function_assert_rules = FunctionItem("List folders that do not contain all requested files",
                                              FolderAssertRules.run(),
                                              ["Enter all name patterns to look for in folders, separated by spaces"])
    menu_divider_file = MenuItem("===FILE UTILITIES===")
    menu_function_rename = FunctionItem("Rename files according to rules",
                                        FileRename.run(),
                                        ["Enter original filename with extension and new filename with extension"])

    # A CommandItem runs a console command
    command_item = CommandItem("Run a console command", "touch hello.txt")

    # A SelectionMenu constructs a menu from a list of strings
    selection_menu = SelectionMenu(["item1", "item2", "item3"])

    # A SubmenuItem lets you add a menu (the selection_menu above, for example)
    # as a submenu of another menu
    submenu_item = SubmenuItem("Submenu item", selection_menu, menu)

    # Once we're done creating them, we just add the items to the menu
    menu.append_item(menu_divider_folder)
    menu.append_item(menu_function_set_icon)
    menu.append_item(menu_function_assert_rules)
    menu.append_item(menu_divider_file)
    menu.append_item(menu_function_rename)

    # Finally, we call show to show the menu and allow the user to interact
    menu.show()

if __name__ == "__main__":
    main()