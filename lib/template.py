from mako.template import Template
from mako.lookup import TemplateLookup

mylookup = None

def lookup():
    # lazy loading and one single instance                                                
    global mylookup
    if mylookup:                                                                          
        return mylookup
                                                                                          
    mylookup = TemplateLookup(
        directories='template/',                                                    
        disable_unicode=True,
        input_encoding='utf8',
        #output_encoding='utf8',                                                          
        #encoding_errors='replace',
        default_filters=['str','h'],
        )
    return mylookup

def serve_template(uri, **kwargs):                                                        
    _t = lookup().get_template(str(uri))                                                  
    if 'self' in kwargs:                                                                  
        kwargs.pop('self')                                                                
    return _t.render(**kwargs)                                                            

def serve_template_fun(uri, func, **kwargs):                                              
    _t = lookup().get_template(str(uri)).get_def(str(func))                               
    if 'self' in kwargs:                                                                  
        kwargs.pop('self')                                                                
    return _t.render(**kwargs)  

st  = serve_template
stf = serve_template_fun

