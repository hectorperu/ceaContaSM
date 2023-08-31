from django.db import models

# Create your models here.


class TblTipoEmpresa(models.Model):
    # Field name made lowercase.
    codigo_tipo_empresa = models.AutoField(primary_key=True)
    # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=30,
                                   db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado', null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'Tbl_Tipo_Empresa'


class Movcontablesdnodomici(models.Model):
    # Field name made lowercase.
    idnodomiciliado = models.AutoField(
        db_column='idNoDomiciliado', primary_key=True)
    # Field name made lowercase.
    movcontable_d = models.CharField(
        db_column='Movcontable_d', max_length=10, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    codunidadeconomica = models.CharField(db_column='CodUnidadEconomica', max_length=10,
                                          db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    tipodoccredfiscal = models.CharField(
        db_column='TipoDocCredFiscal', max_length=2, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    nrodocdua = models.CharField(db_column='NroDocDUA', max_length=45,
                                 db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    anioduacredfiscal = models.CharField(
        db_column='AnioDuaCredFiscal', max_length=4, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    montoretigv = models.DecimalField(
        db_column='MontoRetIGV', max_digits=18, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    pais = models.CharField(db_column='Pais', max_length=7,
                            db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    nombrenodomiciliado = models.CharField(db_column='NombreNoDomiciliado', max_length=100,
                                           db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    rentabruta = models.DecimalField(
        db_column='RentaBruta', max_digits=18, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    deduccioncosto = models.DecimalField(
        db_column='DeduccionCosto', max_digits=18, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    rentaneta = models.DecimalField(
        db_column='RentaNeta', max_digits=18, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    tasaretencion = models.DecimalField(
        db_column='TasaRetencion', max_digits=10, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    impuestoretenido = models.DecimalField(
        db_column='ImpuestoRetenido', max_digits=18, decimal_places=2, blank=True, null=True)
    convenio2imposicion = models.CharField(db_column='Convenio2Imposicion', max_length=7,
                                           db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    tiporenta = models.CharField(db_column='TipoRenta', max_length=7,
                                 db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    aplicaart76 = models.CharField(db_column='AplicaArt76', max_length=1,
                                   db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=1,
                              db_collation='Modern_Spanish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MovContablesDNoDomici'


class TblMovimientocajac(models.Model):
    # Field name made lowercase.
    idmovimientocajac = models.AutoField(
        db_column='idMovimientoCajaC', primary_key=True)
    anio = models.CharField(
        max_length=4, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    mes = models.CharField(
        max_length=2, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    zona = models.CharField(
        max_length=10, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    codunidadeconomica = models.CharField(db_column='codUnidadEconomica', max_length=10,
                                          db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    nrodoc = models.CharField(db_column='NroDoc', max_length=10,
                              db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    fechacontable = models.DateTimeField(
        db_column='FechaContable', blank=True, null=True)
    # Field name made lowercase.
    codmgc = models.CharField(db_column='codMGC', max_length=2,
                              db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    glosa = models.CharField(db_column='Glosa', max_length=200,
                             db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    rucemitido = models.CharField(db_column='RucEmitido', max_length=11,
                                  db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    codigoctabancaria = models.CharField(
        db_column='CodigoCtaBancaria', max_length=12, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    codigotipodocpago = models.CharField(
        db_column='CodigoTipoDocPago', max_length=4, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    nrodocpago = models.CharField(db_column='NroDocPago', max_length=14,
                                  db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    monto = models.DecimalField(
        db_column='Monto', max_digits=18, decimal_places=2, blank=True, null=True)
    transferido = models.CharField(
        max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    correlativo = models.CharField(db_column='Correlativo', max_length=10,
                                   db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=1,
                              db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    transferidoant = models.CharField(
        db_column='TransferidoAnt', max_length=20, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_MovimientoCajaC'


class TblMovimientocajad(models.Model):
    # Field name made lowercase.
    idmovimientocajad = models.AutoField(
        db_column='idMovimientoCajaD', primary_key=True)
    # Field name made lowercase.
    idmovimientocajac = models.ForeignKey(
        TblMovimientocajac, models.DO_NOTHING, db_column='idMovimientoCajaC', blank=True, null=True)
    codunidadeconomica = models.CharField(db_column='CodunidadEconomica', max_length=10,
                                          db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    nrodocumento = models.CharField(db_column='NroDocumento', max_length=10,
                                    db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    fechacontable = models.DateTimeField(
        db_column='FechaContable', blank=True, null=True)
    # Field name made lowercase.
    tipomediopago = models.CharField(
        db_column='TipoMedioPago', max_length=3, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    codpro = models.CharField(
        max_length=14, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    glosa = models.CharField(db_column='Glosa', max_length=250,
                             db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    flujoefectivo = models.CharField(
        db_column='FlujoEfectivo', max_length=10, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    codigodocumentofuente = models.CharField(db_column='CodigoDocumentoFuente', max_length=2,
                                             db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nrodocumentofuente = models.CharField(db_column='NroDocumentoFuente', max_length=14,
                                          db_collation='Modern_Spanish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    fechadocfuente = models.DateTimeField(
        db_column='FechaDocFuente', blank=True, null=True)
    # Field name made lowercase.
    fechavencimiento = models.DateTimeField(
        db_column='FechaVencimiento', blank=True, null=True)
    # Field name made lowercase.
    codigoctabancaria = models.CharField(
        db_column='CodigoCtaBancaria', max_length=12, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    codcuenta = models.CharField(db_column='CodCuenta', max_length=12,
                                 db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    impdebe = models.DecimalField(
        db_column='impDebe', max_digits=18, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    imphaber = models.DecimalField(
        db_column='impHaber', max_digits=18, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    nrooperacion = models.CharField(db_column='NroOperacion', max_length=40,
                                    db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    nrocheque = models.CharField(db_column='NroCheque', max_length=40,
                                 db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    estado = models.CharField(
        max_length=1, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    reparo = models.CharField(
        max_length=1, db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    tipodoc = models.CharField(db_column='TipoDoc', max_length=3,
                               db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    tipooper = models.IntegerField(db_column='TipoOper', blank=True, null=True)
    # Field name made lowercase.
    montoigv = models.DecimalField(
        db_column='MontoIGV', max_digits=12, decimal_places=3, blank=True, null=True)
    # Field name made lowercase.
    montoisc = models.DecimalField(
        db_column='MontoISC', max_digits=10, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    montoretencion4 = models.DecimalField(
        db_column='MontoRetencion4', max_digits=10, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    rigv = models.BooleanField(db_column='RIgv', blank=True, null=True)
    # Field name made lowercase.
    afecto = models.BooleanField(db_column='Afecto', blank=True, null=True)
    # Field name made lowercase.
    costearigv = models.CharField(db_column='CostearIgv', max_length=1,
                                  db_collation='Modern_Spanish_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=90,
                                 db_collation='Modern_Spanish_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_MovimientoCajaD'


class TblAfbaja(models.Model):
    # Field name made lowercase.
    idbaja = models.AutoField(db_column='IdBaja', primary_key=True)
    # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100,
                                   db_collation='Modern_Spanish_CI_AS')
    # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado')

    class Meta:
        managed = False
        db_table = 'Tbl_AFBaja'


class TblAfcargo(models.Model):
    # Field name made lowercase.
    idcargo = models.AutoField(db_column='IdCargo', primary_key=True)
    # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100,
                                   db_collation='Modern_Spanish_CI_AS')
    # Field name made lowercase.
    idempresa = models.IntegerField(
        db_column='idEmpresa')
    # Field name made lowercase.
    estado = models.BooleanField(db_column='Estado')

    class Meta:
        managed = False
        db_table = 'Tbl_AFCargo'
