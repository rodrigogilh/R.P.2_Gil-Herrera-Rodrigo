importar  wx
importar  navegador web

clase  MyApp ( wx . App ):
    def  __init__ ( yo ):
        super (). __init__ ( clearSigInt = True )
        
        # marco de inicio
        yo . InitFrame ()
    
    def  InitFrame ( propio ):
        frame  =  MyFrame ( parent = None , title = "my button app" , pos  = ( 100 , 100 ))
        marco . Mostrar ()


clase  MyFrame ( wx . Frame ):
    # subclase de wx.Window; El marco es una ventana de nivel superior
    # Un marco es una ventana cuyo tamaño y posición pueden (normalmente) ser cambiados por el usuario.
    # Por lo general, representa la primera ventana principal que verá un usuario.
    def  __init__ ( self , parent , title , pos ):
        super (). __init__ ( padre = padre , título = título , pos = pos )
        yo . OnInit ()
    
    def  OnInit ( self ):
        panel  =  MyPanel ( padre = yo )


clase  MyPanel ( wx . Panel ):
    # Un panel es una ventana en la que se colocan los controles. (por ejemplo, botones y cuadros de texto)
    La clase # wx.Panel generalmente se coloca dentro de un objeto wxFrame. Esta clase también se hereda de la clase wxWindow.
    def  __init__ ( yo , padre ):
        super (). __init__ ( padre = padre )
        
        # agregar un mensaje de saludo al panel
        welcomeText  =  wx . StaticText ( self , label = "¡Para aprender wxPython, haga clic en el enlace de abajo!" , Pos = ( 20 , 20 ))

        # agregar un botón para abrir el cuadro de diálogo
        botón  =  wx . Botón ( parent = self , label = 'Click Here!' , Pos  = ( 20 , 120 ))
        botón . Bind ( WX . EVT_BUTTON , sí . OnSubmit ) # unen a la acción botón


    def  onSubmit ( self , event ):
        # cosas para hacer con el botón de enviar
        navegador web . abierto ( 'https://wxpython.org/Phoenix/docs/html/index.html' )
        
if  __name__  ==  "__main__" :
    aplicación  =  MyApp ()
    aplicación . MainLoop ()