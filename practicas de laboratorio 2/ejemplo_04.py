importar  wx


clase  MyApp ( wx . App ):
    def  __init__ ( yo ):
        super (). __init__ ( clearSigInt = True )
        
        # marco de inicio
        yo . InitFrame ()
    
    def  InitFrame ( propio ):
        marco  =  MyFrame ()
        marco . Mostrar ()


clase  MyFrame ( wx . Frame ):
    def  __init__ ( self , title = "MyButtonApp" , pos = ( 100 , 100 )):
        super (). __init__ ( Ninguno , título = título , pos = pos )
        # inicializar el contenido del marco
        yo . OnInit ()

    def  OnInit ( self ):
        yo . panel  =  MyForm ( propio )
        yo . Ajustar ()

clase  MyForm ( wx . Panel ):

    def  __init__ ( yo , padre ):
        super (). __init__ ( padre = padre )

        # Agregue un panel para que se vea correcto en todas las plataformas

        # art proveedor proporciona arte básico https://wxpython.org/Phoenix/docs/html/wx.ArtProvider.html
        bmp  =  wx . ArtProvider . GetBitmap ( id = wx . ART_INFORMATION ,
        cliente = wx . ART_OTHER , tamaño = ( 16 , 16 ))
        titleIco  =  wx . StaticBitmap ( propio , wx . ID_ANY , bmp )
        título  =  wx . StaticText ( self , wx . ID_ANY , 'Mi título' )

        inputOneIco  =  wx . StaticBitmap ( propio , wx . ID_ANY , bmp )
        labelOne  =  wx . StaticText ( self , wx . ID_ANY , 'Entrada 1' )
        yo . inputTxtOne  =  wx . TextCtrl ( self , wx . ID_ANY , value = 'Cuadro de texto' )

        inputTwoIco  =  wx . StaticBitmap ( propio , wx . ID_ANY , bmp )
        labelTwo  =  wx . StaticText ( self , wx . ID_ANY , 'Entrada 2' )
        # wx.SpinCtrl combina wx.TextCtrl y wx.SpinButton en un control.
        yo . inputTwo  =  wx . SpinCtrl ( self , wx . ID_ANY , valor = "0" , min = 0 , max = 100 )

        inputThreeIco  =  wx . StaticBitmap ( propio , wx . ID_ANY , bmp )
        labelThree  =  wx . StaticText ( self , wx . ID_ANY , 'Entrada 3' )
        yo . inputThree  =  wx . Elección ( yo , elecciones = [ 'A' , 'B' , 'C' ])
        

        inputFourIco  =  wx . StaticBitmap ( propio , wx . ID_ANY , bmp )
        labelFour  =  wx . StaticText ( self , wx . ID_ANY , 'Entrada 4' )
        yo . inputFour1  =  wx . CheckBox ( parent = self , label = "Opción 1" )
        yo . inputFour2  =  wx . CheckBox ( parent = self , label = "Opción 2" )
        yo . inputFour3  =  wx . CheckBox ( parent = self , label = "Opción 3" )

        okBtn  =  wx . Botón ( propio , wx . ID_ANY , 'Aceptar' )
        cancelBtn  =  wx . Botón ( propio , wx . ID_ANY , 'Cancelar' )
        yo . Enlazar ( wx . EVT_BUTTON , self . OnOK , okBtn )
        yo . Enlazar ( wx . EVT_BUTTON , self . OnCancel , cancelBtn )

        mainSizer  =  wx . BoxSizer ( wx . VERTICAL )
        titleSizer  =  wx . BoxSizer ( wx . HORIZONTAL )
        inputOneSizer  =  wx . BoxSizer ( wx . HORIZONTAL )
        inputTwoSizer  =  wx . BoxSizer ( wx . HORIZONTAL )
        inputThreeSizer  =  wx . BoxSizer ( wx . HORIZONTAL )
        inputFourSizer  =  wx . BoxSizer ( wx . HORIZONTAL )
        submitBtnSizer  =  wx . BoxSizer ( wx . HORIZONTAL )

        titleSizer . Agregar ( titleIco , 0 , wx . ALL , 5 )
        titleSizer . Agregar ( título , 0 , wx . TODOS , 5 )

        inputOneSizer . Agregar ( inputOneIco , 0 , wx . ALL , 5 )
        inputOneSizer . Agregar ( labelOne , 0 , wx . ALL , 5 )

        inputOneSizer . Agregar ( auto . InputTxtOne , 1 , wx . ALL | wx . EXPAND , 5 )

        inputTwoSizer . Agregar ( inputTwoIco , 0 , wx . ALL , 5 )
        inputTwoSizer . Agregar ( labelTwo , 0 , wx . ALL , 5 )
        inputTwoSizer . Agregar ( auto . InputTwo , 1 , wx . ALL | wx . EXPAND , 5 )

        inputThreeSizer . Agregar ( inputThreeIco , 0 , wx . ALL , 5 )
        inputThreeSizer . Agregar ( labelThree , 0 , wx . ALL , 5 )
        inputThreeSizer . Agregar ( auto . InputThree , 1 , wx . ALL | wx . EXPAND , 5 )

        inputFourSizer . Agregar ( inputFourIco , 0 , wx . ALL , 5 )
        inputFourSizer . Agregar ( labelFour , 0 , wx . ALL , 5 )
        inputFourSizer . Agregar ( auto . InputFour1 , 1 , wx . ALL | wx . EXPAND , 5 )
        inputFourSizer . Sumar ( auto . InputFour2 , 1 , wx . ALL | wx . EXPAND , 5 )
        inputFourSizer . Agregar ( auto . InputFour3 , 1 , wx . ALL | wx . EXPAND , 5 )

        submitBtnSizer . Agregar ( okBtn , 0 , wx . ALL , 5 )
        submitBtnSizer . Agregar ( cancelBtn , 0 , wx . ALL , 5 )

        mainSizer . Agregar ( titleSizer , 0 , wx . CENTER )
        mainSizer . Sumar ( wx . StaticLine ( self ,), 0 , wx . ALL | wx . EXPAND , 5 )
        mainSizer . Agregar ( inputOneSizer , 0 , wx . ALL | wx . EXPAND , 5 )
        mainSizer . Agregar ( inputTwoSizer , 0 , wx . ALL | wx . EXPAND , 5 )
        mainSizer . Agregar ( inputThreeSizer , 0 , wx . ALL | wx . EXPAND , 5 )
        mainSizer . Agregar ( inputFourSizer , 0 , wx . ALL | wx . EXPAND , 5 )
        mainSizer . Sumar ( wx . StaticLine ( propio ), 0 , wx . ALL | wx . EXPAND , 5 )
        mainSizer . Agregar ( submitBtnSizer , 0 , wx . ALL | wx . CENTER , 5 )

        yo . SetSizer ( mainSizer )
        mainSizer . Encajar ( yo )
        yo . Diseño ()


    def  onOK ( yo , evento ):
        # Hacer algo
        print ( 'controlador onOK' )
        datos  =  self . getData ()
        imprimir ( datos )

    def  onCancel ( self , event ):
        yo . closeProgram ()

    def  closeProgram ( self ):
        # self.GetParent () obtendrá el marco que
        # tiene el método .Close () para cerrar el programa
        yo . GetParent (). Cerrar ()

    def  getData ( self ):
        '' '
        esto aquí obtendrá datos de todos los botones
        '' '
        datos  = []
        datos . añadir ( self . inputTxtOne . GetValue ())
        datos . añadir ( self . inputTwo . GetValue ())
        selección  =  self . inputThree . GetSelection ()
        datos . añadir (( selección ,
                    yo . inputThree . GetString ( selección ))
                    )
        datos . añadir ( self . inputFour1 . GetValue ())
        datos . añadir ( self . inputFour2 . GetValue ())
        datos . añadir ( self . inputFour3 . GetValue ())
        devolver  datos

# Ejecuta el programa
if  __name__  ==  '__main__' :
    aplicación  =  MyApp ()
    aplicación . MainLoop ()