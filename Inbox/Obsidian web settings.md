![](chrome-extension://edoacekkjanmingkbkgjndndibhkegad/icon48.png)

# Obsidian Web Settings

**You are running Obsidian Web in an unsupported environment!** Obsidian Web is tested only on recent versions of Chrome, and no guarantees are made by the maintainers of this project that it might work on any other browser â€” even other Chrome derivatives. Some features may not work correctly as a result, but you can feel free to [start a new discussion](https://github.com/coddingtonbear/obsidian-web/discussions/new?category=exotic-browser-support) if you run into difficulty â€” members of the community may be able to help!

Obsidian Web integrates with Obsidian via the interface provided by the [Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) plugin. Before beginning to use this, you will want to install and enable that plugin from within Obsidian.

Hostname

Hostname

Hostname on which Obsidian is running (usually 127.0.0.1).

API Key

You can find your API key in the 'Local REST API' section of your settings in Obsidian.

A valid API key from Obsidian Local REST API is required.

This browser extension does not have permission for the host `127.0.0.1`.GRANT PERMISSIONS

## Keyboard Shortcut

You can launch Obsidian Web by pressing `Alt+Shift+O`. If you would like to select a different shortcut, you can do so via [Chrome's shortcut settings](chrome-extension://edoacekkjanmingkbkgjndndibhkegad/options.html#).

## Note Recall

Have you been to this page before? Maybe you already have notes about it. Enabling this feature will let this extension search your notes for references to the URL you are visiting.

**Search for previous notes about this page when you activate the extension?** If enabled, [Page Notes](https://github.com/coddingtonbear/obsidian-web/wiki/Page-Notes) for the URL you are currently visiting, and pages on which you've mentioned the URL you are visiting will be shown to you in the dialog when you activate the extension.

**Search for previous notes about linked pages when you hover over links? [(docs)](https://github.com/coddingtonbear/obsidian-web/wiki/Hover-Messages)** If enabled, a tooltip will be displayed when hovering over links targeting pages you have created [Page Notes](https://github.com/coddingtonbear/obsidian-web/wiki/Page-Notes) for or have mentioned in a note. The displayed message can be customized using `web-message` and other frontmatter fields.

Requires extra permissions

**Search for previous notes about this page in the background? [(docs)](https://github.com/coddingtonbear/obsidian-web/wiki/Extension-Badge-Messages)** If enabled, [Page Notes](https://github.com/coddingtonbear/obsidian-web/wiki/Page-Notes) for the URL you are currently visiting, and pages on which you've mentioned the URL you are visiting will be searched for as you browse. If a matching note is found, a badge will be shown on the extension icon.

Requires extra permissions

### Automatically Display Matches [(docs)](https://github.com/coddingtonbear/obsidian-web/wiki/Automatic-Match-Display)

Do you want to be shown a message when the URL you are visiting has a [Page Note](https://github.com/coddingtonbear/obsidian-web/wiki/Page-Notes) or has been mentioned in a note? You can configure conditions in which the dialog will be opened automatically to let you know when you have been to this URL before. This feature requires that background searches be enabled.

Requires extra permissions

Never open the dialog automatically

â€‹

### Template Suggestions

**Suggest a template when a [Page Note](https://github.com/coddingtonbear/obsidian-web/wiki/Page-Notes) for the current URL is found?** When the URL of the page you are visiting has been found to have a [Page Note](https://github.com/coddingtonbear/obsidian-web/wiki/Page-Notes), suggest a template for updating the existing note? This feature requires that you have enabled search features.CONFIGURE TEMPLATE TO USE FOR PAGE NOTES

**Suggest a template when a note mentioning this URL is found?** When the URL of the page you are visiting has been found in the content of a note in your vault, suggest a template for updating the existing note? This feature requires that you enable search features.CONFIGURE TEMPLATE TO USE FOR MENTIONS

## Templates [(docs)](https://github.com/coddingtonbear/obsidian-web/wiki/Understanding-Templates)

You can configure multiple templates for use when inserting content into Obsidian. Each template describes how to convert information about the current tab into content for insertion into your notes.

||Name|Options|
|---|---|---|
||Append to current daily note||
||Create new note||
||Capture page snapshot||
||||

**Protip:** Looking for ideas about how you can use this plugin to improve your workflow; have a look at the [Wiki](https://github.com/coddingtonbear/obsidian-web/wiki) and [Discussions](https://github.com/coddingtonbear/obsidian-web/discussions) for tips.