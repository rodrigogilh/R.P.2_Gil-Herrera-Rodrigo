importar  wx


clase  MyApp ( wx . App ):
    def  __init__ ( yo ):
        super (). __init__ ()

    def  OnInit ( self ):
        frame  =  MyFrame ( parent = None , title = "Este es un marco" )
        marco . Mostrar ()
        volver  verdadero


clase  MyFrame ( wx . Frame ):
    # subclase de wx.Window; El marco es una ventana de nivel superior
    # Un marco es una ventana cuyo tamaño y posición pueden (normalmente) ser cambiados por el usuario.
    # Por lo general, representa la primera ventana principal que verá un usuario.
    def  __init__ ( yo , padre , título ):
        super (). __init__ ( padre = padre , título = título , pos  = ( 100 , 100 ))

        yo . OnInit ()

    def  OnInit ( self ):
        panel  =  MyPanel ( propio )


clase  MyPanel ( wx . Panel ):
    # Un panel es una ventana en la que se colocan los controles. (por ejemplo, botones y cuadros de texto)
    La clase # wx.Panel generalmente se coloca dentro de un objeto wxFrame. Esta clase también se hereda de la clase wxWindow.
    def  __init__ ( yo , padre ):
        super (). __init__ ( padre = padre )
        yo . _dont_show  =  False  # para el cuadro de diálogo del mensaje
        
        # agregar un mensaje de saludo al panel
        welcomeText  =  wx . StaticText ( self , label = "¡Hola mundo!" , Pos = ( 20 , 20 ))

        # agregar un cuadro de texto
        yo . _text  =  wx . TextCtrl ( parent =  self , value  =  'INGRESE ALGUNO TEXTO AQUÍ' , pos  = ( 20 , 60 ), size = ( 300 , 50 ))

        # agregar un botón para abrir el cuadro de diálogo
        yo . _button  =  wx . Botón ( parent = self , label = 'Submit' , pos  = ( 20 , 120 ))
        yo . _button . Bind ( WX . EVT_BUTTON , sí . OnSubmit ) # unen a la acción botón


    def  ShowDialog ( self ):
        # ¡Aparece una ventana de diálogo de mensaje al enviar!
        si  yo . _dont_show :
            regresar  Ninguno

        dlg  =  wx . RichMessageDialog ( parent = None ,
                message =  "¿Estás listo para aprender wxPython?" ,
                título = "wxPythonStuff" ,
                estilo = wx . YES_NO | wx . CANCELAR | wx . CENTRO )
        dlg . ShowCheckBox ( "No mostrar esto de nuevo" )
        dlg . ShowModal () # muestra el diálogo

        si  dlg . IsCheckBoxChecked ():
            print ( "¿Está marcada la casilla de verificación?" , dlg . IsCheckBoxChecked ())
            yo . _dont_show = Verdadero
    

    def  onSubmit ( self , event ):
        # cosas para hacer con el botón de enviar
        print ( self . _text . GetValue ())
        yo . ShowDialog ()
        
if  __name__  ==  "__main__" :

    aplicación  =  MyApp ()
    frame  =  MyFrame ( parent = None , title = "Este es un marco" )
    aplicación . MainLoop ()