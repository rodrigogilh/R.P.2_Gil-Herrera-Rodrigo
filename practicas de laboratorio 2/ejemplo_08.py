def  createMenu ( self ):
        menuBar  =  wx . MenuBar ()

        fileMenu  =  wx . Menú () # primero
        newItem  =  wx . MenuItem ( parentMenu = fileMenu , id = wx . ID_NEW ,
                text = 'Nueva página \ t Ctrl + N' , helpString = 'Crear nueva página' ,
                tipo = wx . ITEM_NORMAL ) # subMenu es la opción final
        fileMenu . Anexar ( newItem )
        yo . Enlazar ( evento = wx . EVT_MENU , controlador = self . OnNewItem , fuente = newItem )

        # finalmente, agregue el menú Archivo
        menuBar . Adjuntar ( fileMenu , '& File' )

        # finalmente, agregue la barra de menú
        yo . SetMenuBar ( menuBar )

    def  onNewItem ( self , evento ):
        
        count  =  self . nb . GetPageCount () +  1  # agregue 1 para una página adicional
        message  =  "Esta es la página {}" . formato ( recuento )
        page  =  NBPage ( self . nb , mensaje )
        yo . nb . AddPage ( página , "Página"  +  str ( recuento ))



if  __name__  ==  "__main__" :
    aplicación  =  MyApp ()
    aplicación . MainLoop ()