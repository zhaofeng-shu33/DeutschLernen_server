import os

from lxml import etree

from DeutschLernen.settings import BASE_DIR

def xslt_render(xml_str, render_method):
    if(render_method[0] == 'N'):
        if(len(render_method) > 1 and render_method[1] == 'E'): # can be edited
            xslt_root_file = os.path.join(BASE_DIR, 'templates', 'NounEditTemplate.xslt')
        else:
            xslt_root_file = os.path.join(BASE_DIR, 'templates', 'NounRenderTemplate.xslt')            
    elif(render_method[0] == 'V'):
        xslt_root_file = os.path.join(BASE_DIR, 'templates', 'VerbRenderTemplate.xslt')
    elif(render_method[0] == 'A'):
        xslt_root_file = os.path.join(BASE_DIR, 'templates', 'AdjRenderTemplate.xslt')
    else:
        return 'invalid render method'
    xslt_root = etree.parse(xslt_root_file)
    transform=etree.XSLT(xslt_root)
    xml_doc=etree.fromstring(xml_str.encode('utf-8'))
    result_tree=transform(xml_doc)
    print(transform.error_log)
    return etree.tostring(result_tree,pretty_print=True).decode('utf-8')
