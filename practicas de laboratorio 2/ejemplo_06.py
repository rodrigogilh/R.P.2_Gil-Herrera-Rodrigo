importar  wx
desde  wx  import  html2

clase  MyApp ( wx . App ):
    def  OnInit ( self ):
        WebFrame ( Ninguno , "Navegar por la Web" ). Mostrar ()
        volver  verdadero


clase  WebFrame ( wx . Frame ):
    def  __init__ ( yo , padre , título ):
        super (). __init__ ( padre , título = título )
        
        yo . _browser  =  html2 . WebView . Nuevo ( yo )
        yo . _browser . LoadURL ( "www.google.com" ) # página de inicio
        yo . _bar  =  NavBar ( self , self . _browser )
        
        
        calibrador  =  wx . BoxSizer ( wx . VERTICAL )
        calibrador . Agregar ( self . _Bar , 0 , wx . EXPAND )
        calibrador . Agregar ( self . _Browser , 1 , wx . EXPAND )
        yo . SetSizer ( medidor )
        
        yo . Enlazar ( html2 . EVT_WEBVIEW_TITLE_CHANGED , self . OnTitle )

    def  OnTitle ( self , event ):
        yo . Título  =  evento . GetString ()



clase  NavBar ( wx . Panel ):
    def  __init__ ( yo , padre , navegador ):
        super (). __init__ ( padre )

        yo . browser  =  navegador
        imprimir ( "URL actual:" , sí . navegador . GetCurrentURL ())
        yo . _url  =  wx . TextCtrl ( self , style = wx . TE_PROCESS_ENTER )
        yo . _url . SetHint ( "Ingrese la URL aquí y presione enter ..." )
        yo . _url . Enlazar ( wx . EVT_TEXT_ENTER , self . OnEnter )

        espalda  =  wx . Botón ( auto , estilo = wx . BU_EXACTFIT )
        volver . Mapa de bits  =  wx . ArtProvider . GetBitmap ( wx . ART_GO_BACK ,
                                               wx . ART_TOOLBAR )
        volver . Enlazar ( wx . EVT_BUTTON , self . GoBack )

        fw  =  wx . Botón ( auto , estilo = wx . BU_EXACTFIT )
        fw . Mapa de bits  =  wx . ArtProvider . GetBitmap ( wx . ART_GO_FORWARD ,
                                             wx . ART_TOOLBAR )
        fw . Enlazar ( wx . EVT_BUTTON , self . GoForward )

        calibrador  =  wx . BoxSizer ( wx . HORIZONTAL )
        calibrador . Sumar ( reverso , proporción = 0 , bandera = wx . TODOS , borde = 5 )
        calibrador . Sumar ( fw , proporción = 0 , bandera = wx . TODOS , borde = 5 )
        calibrador . Agregar ( ventana = self . _Url , proporción = 1 , bandera = wx . EXPAND )
        yo . SetSizer ( medidor )


    def  onEnter ( self , event ):
        yo . navegador . LoadURL ( auto . _Url . Valor )
    
    def  goBack ( self , event ):
        evento . Habilitar ( auto . Navegador . CanGoBack ())
        yo . navegador . Regresar ()

    def  goForward ( self , event ):
        evento . Habilitar ( auto . Navegador . CanGoForward ())
        yo . navegador . Adelante ()



if  __name__  ==  "__main__" :
    aplicación  =  MyApp ()
    aplicación . MainLoop ()