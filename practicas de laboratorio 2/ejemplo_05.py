importar sistema  operativo
importar  wx  

clase  MyApp ( wx . App ):
    def  __init__ ( yo ):
        super (). __init__ ()

        frame  =  MyFrame ( parent = None , title = "Aplicación de barra de menú" )
        marco . Mostrar ()


clase  FileMenu ( wx . Menú ):
    def  __init__ ( self , parentFrame ):
        super (). __init__ ()
        yo . OnInit ()
        yo . parentFrame  =  parentFrame
    
    def  OnInit ( self ):
        newItem  =  wx . MenuItem ( parentMenu = self , id = wx . ID_NEW , text = "& New \ t Ctrl + N" , kind = wx . ITEM_NORMAL )
        yo . Anexar ( newItem )

        openItem  =  wx . MenuItem ( parentMenu = self , id = wx . ID_OPEN , text = '& Open \ t Ctrl + O' , kind = wx . ITEM_NORMAL )
        yo . Adjuntar ( openItem )
        yo . Enlazar ( wx . EVT_MENU , handler = self . OnOpen , source = openItem )

        saveItem  =  wx . MenuItem ( parentMenu = self , id = wx . ID_SAVE , text = "& Save \ t Ctrl + S" , helpString = "Guarde su archivo" , kind = wx . ITEM_NORMAL )
        yo . Anexar ( saveItem )
        yo . Enlazar ( wx . EVT_MENU , handler = self . OnSave , source = saveItem )

        yo . AppendSeparator ()

        radioItem1  =  wx . MenuItem ( self , id = 200 , text  =  "Option 1" , kind  =  wx . ITEM_RADIO )
        yo . Adjuntar ( radioItem1 )
        radioItem2  =  wx . MenuItem ( self , id = 300 , text  =  "Option 2" , kind  =  wx . ITEM_RADIO )
        yo . Adjuntar ( radioItem2 )

        yo . AppendSeparator ()
        
        quitItem  =  wx . MenuItem ( parentMenu = self , id = wx . ID_EXIT , text = '& Salir \ t Ctrl + Q' )
        yo . Adjuntar ( quitItem )
        yo . Enlazar ( wx . EVT_MENU , handler = self . OnQuit , source = quitItem )

    def  onOpen ( self , event ):
        comodín  =  "archivos TXT (* .txt) | * .txt"
        diálogo  =  wx . FileDialog ( self . ParentFrame , "Abrir archivos de texto" , comodín = comodín ,
                               estilo = wx . FD_OPEN  |  wx . FD_FILE_MUST_EXIST )

        si  diálogo . ShowModal () ==  wx . ID_CANCEL :
            regresar  Ninguno

        ruta  =  diálogo . GetPath ()
        si  os . camino . existe ( ruta ):
            con  open ( ruta ) como  myfile :
                para la  línea  en  myfile :
                    yo . parentFrame . texto . WriteText ( línea )

    def  onSave ( self , event ):
        diálogo  =  wx . FileDialog ( self . ParentFrame , message = "Guarde sus datos" ,
                            defaultFile = "Untitled.txt" , style = wx . FD_SAVE  |  wx . FD_OVERWRITE_PROMPT )

        si  diálogo . ShowModal () ==  wx . ID_CANCEL :
            regresar  Ninguno
        
        ruta  =  diálogo . GetPath ()
        datos  =  self . parentFrame . texto . GetValue ()
        imprimir ( datos )
        datos  =  datos . dividir ( ' \ n ' )
        imprimir ( datos )
        con  open ( ruta , "w +" ) como  miarchivo :
            para  la línea  en  los datos :
                myfile . escribir ( línea + " \ n " )


    def  onQuit ( self , event ):
        yo . parentFrame . Cerrar ()


clase  EditMenu ( wx . Menú ):
    def  __init__ ( yo ):
        super (). __init__ ()
        yo . OnInit ()

    def  OnInit ( self ):
        copyItem  =  wx . MenuItem ( self , 100 , text  =  "Copiar" , kind  =  wx . ITEM_NORMAL )
        yo . Anexar ( CopyItem )
        cutItem  =  wx . MenuItem ( self , 101 , text  =  "Cut" , kind  =  wx . ITEM_NORMAL )
        yo . Anexar ( cutItem )
        pasteItem  =  wx . MenuItem ( self , 102 , text  =  "Paste" , kind  =  wx . ITEM_NORMAL )
        yo . Anexar ( pasteItem )
    

clase  MyFrame ( wx . Frame ):         
    def  __init__ ( yo , padre , título ):
        super (). __init__ ( padre , título  =  título , tamaño  = ( 500 , 400 ))  
        yo . InitUI ()
         
    def  InitUI ( propio ):   
        yo . texto  =  wx . TextCtrl ( parent = self , id = wx . ID_ANY , style  =  wx . EXPAND | wx . TE_MULTILINE )
        menuBar  =  wx . MenuBar ()

        fileMenu  =  FileMenu ( parentFrame = self )
        menuBar . Adjuntar ( fileMenu , '& File' )

        editMenu  =  EditMenu ()
        menuBar . Append ( editMenu , '& Editar' )

        yo . SetMenuBar ( menuBar )

        # self.Bind (wx.EVT_MENU, self.MenuHandler)
        yo . Centro ()
        yo . Mostrar ( verdadero )


if  __name__  ==  '__main__' :
    aplicación  =  MyApp ()
    aplicación . MainLoop ()