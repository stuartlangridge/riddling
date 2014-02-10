from xml.dom import minidom
import os, subprocess

def main():
    configxml = os.path.join(os.path.dirname(__file__), "www", "config.xml")
    fp = open(configxml)
    data = fp.read()
    fp.close()
    dom = minidom.parseString(data)
    svg = os.path.join(os.path.dirname(__file__), "resources", "Riddling.svg")
    for iconel in dom.documentElement.getElementsByTagName("icon"):
        parts = iconel.getAttribute("src").split("/")
        fn = os.path.join(os.path.dirname(__file__), "www", *parts)
        fol = os.path.dirname(fn)
        width = int(iconel.getAttribute("width"))
        height = int(iconel.getAttribute("height"))
        try:
            os.makedirs(fol)
        except OSError as e:
            if e.errno == 17: 
                pass
            else:
                raise
        newsize = "%sx%s" % (width, height)
        cmd = ["convert", svg, "-resize", newsize, fn]
        print "Creating %sx%s icon as %s" % (width, height, fn)
        subprocess.call(cmd)

if __name__ == "__main__":
    main()