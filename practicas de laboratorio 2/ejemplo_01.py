importar  wx

aplicación  =  wx . Aplicación ( clearSigInt = True ) # clearSigInt para permitir terminar el programa con CTRL + C
marco  =  wx . Marco ( padre = Ninguno , título = "" ) ## objeto de la ventana principal
panel  =  wx . Panel ( padre = marco )
texto  =  wx . StaticText ( parent = panel , label = "Hello, from wxPython !!" , pos  = ( 40 , 40 ))
marco . Mostrar ()
aplicación . MainLoop ()

importar  wx
importar  navegador web

clase  MyApp ( wx . App ):
    def  __init__ ( yo ):
        super (). __init__ ( clearSigInt = True )
        
        # marco de inicio
        yo . InitFrame ()
    
    def  InitFrame ( propio ):
        frame  =  MyFrame ( parent = None , title = "Basic Frame" , pos = ( 100 , 100 ))
        marco . Mostrar ( verdadero )


clase  MyFrame ( wx . Frame ):
    # subclase de wx.Window; El marco es una ventana de nivel superior
    # Un marco es una ventana cuyo tamaño y posición pueden (normalmente) ser cambiados por el usuario.
    # Por lo general, representa la primera ventana principal que verá un usuario.
    def  __init__ ( self , parent , title , pos = pos ):
        super (). __init__ ( padre = padre , título = título , pos = pos )
    
    def  OnInit ( self ):
        panel  =  MyPanel ( padre = yo )