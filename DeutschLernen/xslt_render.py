from lxml import etree
def xslt_render(xml_str,render_method):
    if(render_method[0]=='N'):
        if(render_method[1]=='V'):
            xslt_root=etree.parse('templates/NounRenderTemplate.xslt')
        elif(render_method[1]=='E'):
            xslt_root=etree.parse('templates/NounEditTemplate.xslt')            
        transform=etree.XSLT(xslt_root)
        xml_doc=etree.fromstring(xml_str)
        result_tree=transform(xml_doc)
        return etree.tostring(result_tree,pretty_print=True).decode('utf-8')
