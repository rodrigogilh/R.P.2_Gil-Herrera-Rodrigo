importar  wx
importar  wx . grid  como  gridlib
importar  csv

clase  MyApp ( wx . App ):
    def  __init__ ( yo ):
        super (). __init__ ( clearSigInt = True )
        
        # marco de inicio
        yo . InitFrame ()
    
    def  InitFrame ( propio ):
        frame  =  MyFrame ( parent = None , title = "Basic Frame" )
        marco . Mostrar ( verdadero )


clase  MyFrame ( wx . Frame ):
    def  __init__ ( yo , padre , título ):
        super (). __init__ ( padre = padre , título = título )
        yo . OnInit ()

    def  OnInit ( self ):
        # primero crea un panel ficticio para contener texto
        titlePanel  =  MyPanel ( padre = yo )

        # crear medidores para controlar el diseño
        mainSizer  =  wx . BoxSizer ( wx . VERTICAL )
        titleSizer  =  wx . BoxSizer ( wx . HORIZONTAL )
        gridSizer  =  wx . BoxSizer ( wx . HORIZONTAL )

        titleSizer . Agregar ( titlePanel , 0 , wx . ALL , 5 )
        mainSizer . Agregar ( titleSizer , 0 , wx . CENTER )
        mainSizer . Sumar ( wx . StaticLine ( self ,), 0 , wx . ALL | wx . EXPAND , 5 )

        # visor de datos
        grid  =  GridTable ( propio )
        cuadrícula . LoadFile ()
        cuadrícula . SetColReadOnly ( 0 )
        gridSizer . Sumar ( cuadrícula , 1 , wx . ALL | wx . EXPAND , 5 )
        mainSizer . Agregar ( gridSizer , 0 , wx . ALL | wx . EXPAND , 5 )

        yo . SetSizer ( mainSizer )
        mainSizer . Encajar ( yo )


clase  MyPanel ( wx . Panel ):
    def  __init__ ( yo , padre ):
        super (). __init__ ( padre = padre )
        welcomeText  =  wx . StaticText ( self , label = "Data Grid Display" , pos = ( 20 , 20 ))



clase  GridTableSource ( gridlib . GridTableBase ):
    def  __init__ ( yo ):
        super (). __init__ ()
        yo . _data  =  Ninguno
        yo . _header  =  Ninguno
        yo . _readOnly  =  lista ()

    def  LoadFile ( self , fileName = './sample_data.csv' ):
        fileName  =  './sample_data.csv'
        lector  =  csv . lector ( open ( fileName , 'r' ))
        yo . _data  = [ fila  por  fila  en el  lector ]
        yo . _header  =  self . _data . pop ( 0 )
        yo . _readOnly  =  lista ()
    
    def  Ordenar ( self , col , ascendente ):
        # self._data.sort (key = lambda data: data [col], reverse = True)
        pasar

    def  SetColReadOnly ( self , col ):
        yo . _readOnly . añadir ( col )

    def  GetNumberRows ( self ):
        return  len ( self . _data ) si  self . _data  else  0

    def  GetNumberCols ( self ):
        return  len ( self . _header ) si  self . _header  else  0

    def  GetValue ( self , row , col ):
        si  no  uno mismo . _data :
            volver  ""
        otra cosa :
            volver a  sí mismo . _data [ fila ] [ col ]

    def  SetValue ( self , row , col , value ):
        si  yo . _data :
            yo . _data [ fila ] [ col ] =  valor

    def  GetColLabelValue ( self , col ):
        volver a  sí mismo . _header [ col ] if  self . _header  else  Ninguno



clase  GridTable ( gridlib . Grid ):
    def  __init__ ( yo , padre ):
        super (). __init__ ( padre )

        yo . _data  =  GridTableSource ()
        yo . SetTable ( self . _Data )

        # necesidad de implementar un evento de clasificación; más error de falla de sementación
        yo . Enlazar ( gridlib . EVT_GRID_COL_SORT , self . OnSort )

    def  OnSort ( self , event ):
        yo . _data . Ordenar ( evento . Col ,
                        yo . IsSortOrderAscending ())

    def  LoadFile ( self , fileName = './sample_data.csv' ):
        yo . _data . LoadFile ( nomArchivo )
        yo . SetTable ( self . _Data )
        yo . AutoSizeColumns ()


    def  SetColReadOnly ( self , col ):
        yo . _data . SetColReadOnly ( col )


if  __name__  ==  "__main__" :
    aplicación  =  MyApp ()
    aplicación . MainLoop ()










importar  csv
desde  io  import  StringIO
importar  wx
importar  wx . grid  como  gridlib

clase  CSVDataSource ( gridlib . GridTableBase ):
    def  __init__ ( yo ):
        super (). __init__ ()
        yo . _data  =  Ninguno
        yo . _header  =  Ninguno
        yo . _readOnly  =  lista ()
        
        yo . _roAttr  =  gridlib . GridCellAttr ()
        yo . _roAttr . SetReadOnly ()
        c  =  wx . SystemSettings . GetColour ( wx . SYS_COLOUR_GRAYTEXT )
        yo . _roAttr . TextColour  =  c

    def  LoadFile ( self , fileName = './sample_data.csv' ):
        fileName  =  './sample_data.csv'
        lector  =  csv . lector ( open ( fileName , 'r' ))
        yo . _data  = [ fila  por  fila  en el  lector ]
        yo . _header  =  self . _data . pop ( 0 )
        yo . _readOnly  =  lista ()

    def  GetData ( self ):
        si  no  uno mismo . _data :
            volver  ""

        buff  =  StringIO ()
        escritor  =  csv . escritor ( aficionado )
        escritor . Writerow ( self . _header )
        escritor . Writerows ( self . _data )
        imprimir ( buff . getvalue ())
        volver  buff . getvalue ()

    def  SetColReadOnly ( self , col ):
        yo . _readOnly . añadir ( col )

    def  GetAttr ( self , row , col , kind ):
        si  col  en  uno mismo . _readOnly :
            yo . _roAttr . IncRef ()
            volver a  sí mismo . _roAttr
        regresar  Ninguno

    def  Ordenar ( self , col , ascendente ):
        yo . _data . ordenar ( Ninguno , datos lambda  : datos [ col ], no ascendente ) 

    def  GetNumberRows ( self ):
        return  len ( self . _data ) si  self . _data  else  0

    def  GetNumberCols ( self ):
        return  len ( self . _header ) si  self . _header  else  0

    def  GetValue ( self , row , col ):
        si  no  uno mismo . _data :
            volver  ""
        otra cosa :
            volver a  sí mismo . _data [ fila ] [ col ]

    def  SetValue ( self , row , col , value ):
        si  yo . _data :
            yo . _data [ fila ] [ col ] =  valor

    def  GetColLabelValue ( self , col ):
        volver a  sí mismo . _header [ col ] if  self . _header  else  Ninguno

clase  CSVEditorGrid ( gridlib . Grid ):
    def  __init__ ( yo , padre ):
        super (). __init__ ( padre )

        yo . _data  =  CSVDataSource ()
        yo . SetTable ( self . _Data )

        yo . Enlazar ( gridlib . EVT_GRID_COL_SORT , self . OnSort )

    def  OnSort ( self , event ):
        yo . _data . Ordenar ( evento . Col ,
                        yo . IsSortOrderAscending ())

    def  LoadFile ( self , fileName ):
        yo . _data . LoadFile ( nomArchivo )
        yo . SetTable ( self . _Data )
        yo . AutoSizeColumns ()

    def  SaveFile ( self , fileName ):
        con  open ( fileName , 'w +' ) como  fileObj :
            fileObj . escribir ( self . _data . GetData ())

    def  SetColReadOnly ( self , col ):
        yo . _data . SetColReadOnly ( col )

# ------- Aplicación de muestra --------- #

clase  MyFrame ( wx . Frame ):
    def  __init__ ( yo , padre , título ):
        super ( MyFrame , yo ). __init__ ( padre , título = título )

        menub  =  wx . MenuBar ()
        fmenu  =  wx . Menú ()
        fmenu . Adjuntar ( wx . ID_OPEN )
        fmenu . Adjuntar ( wx . ID_SAVE )
        menub . Append ( fmenu , "Archivo" )
        yo . SetMenuBar ( menub )
        yo . CreateStatusBar ()

        calibrador  =  wx . BoxSizer ()
        yo . _file  =  'sample_data.csv'
        yo . _grid  =  CSVEditorGrid ( propio )
        yo . _grid . LoadFile ( self . _File )
        yo . _grid . SetColReadOnly ( 0 )
        
        calibrador . Agregar ( self . _Grid , 1 , wx . EXPAND )
        yo . SetSizer ( medidor )
        yo . SetInitialSize ()
        
        yo . Enlazar ( wx . EVT_MENU , self . OnSave , id = wx . ID_SAVE )
        yo . Enlazar ( wx . EVT_MENU , self . OnOpen , id = wx . ID_OPEN )

    def  OnOpen ( self , event ):
        dlg  =  wx . FileDialog ( self , "Abrir archivo CSV" , comodín = "* .csv" )
        resultado  =  dlg . ShowModal ()
        si  resultado  ==  wx . ID_OK :
            yo . _grid . LoadFile ( dlg . Path )
        dlg . Destruir ()

    def  OnSave ( self , event ):
        yo . _grid . SaveFile ( self . _File )
        yo . SetStatusText ( "Archivo guardado:% s"  %  self . _File )

clase  MyApp ( wx . App ):
    def  OnInit ( self ):
        yo . frame  =  MyFrame ( Ninguno , título = "Cuadrícula de datos" )
        yo . marco . Mostrar ();
        volver  verdadero

if  __name__  ==  "__main__" :
    app  =  MyApp ( falso )
    aplicación . MainLoop ()