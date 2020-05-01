# coding=gbk
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


# class Data0(models.Model):
#     海关编号 = models.CharField(max_length=255, blank=True, null=True)
#     商品序号 = models.CharField(max_length=255, blank=True, null=True)
#     商品编号 = models.CharField(max_length=255, blank=True, null=True)
#     商品名称 = models.CharField(max_length=255, blank=True, null=True)
#     商品规格型号 = models.CharField(max_length=255, blank=True, null=True)
#     第一法定计量单位 = models.CharField(max_length=255, blank=True, null=True)
#     申报日期 = models.CharField(max_length=255, blank=True, null=True)
#     实征从价关税率 = models.CharField(max_length=255, blank=True, null=True)
#     应征从价关税率 = models.CharField(max_length=255, blank=True, null=True)
#     每项商品需要监管证件 = models.CharField(max_length=255, blank=True, null=True)
#     产销国 = models.CharField(max_length=255, blank=True, null=True)
#     经营单位编号 = models.CharField(max_length=255, blank=True, null=True)
#     经营单位名称 = models.CharField(max_length=255, blank=True, null=True)
#     货主单位代码 = models.CharField(max_length=255, blank=True, null=True)
#     货主单位名称 = models.CharField(max_length=255, blank=True, null=True)
#     申报单位代码 = models.CharField(max_length=255, blank=True, null=True)
#     申报单位名称 = models.CharField(max_length=255, blank=True, null=True)
#     监管方式 = models.CharField(max_length=255, blank=True, null=True)
#     实征从量关税税率 = models.CharField(max_length=255, blank=True, null=True)
#     应征从量关税税率 = models.CharField(max_length=255, blank=True, null=True)
#     实征从价增值税率 = models.CharField(max_length=255, blank=True, null=True)
#     应征从价增值税率 = models.CharField(max_length=255, blank=True, null=True)
#     实征从价消费税率 = models.CharField(max_length=255, blank=True, null=True)
#     应征从价消费税率 = models.CharField(max_length=255, blank=True, null=True)
#     实征从量消费税税率 = models.CharField(max_length=255, blank=True, null=True)
#     应征从量消费税税率 = models.CharField(max_length=255, blank=True, null=True)
#     实征从价反倾销税税率 = models.CharField(max_length=255, blank=True, null=True)
#     应征从价反倾销税税率 = models.CharField(max_length=255, blank=True, null=True)
#     关税完税价 = models.CharField(max_length=255, blank=True, null=True)
#     第一法定数量 = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'data0'
#
#
# class Data1(models.Model):
#     海关编号 = models.CharField(max_length=255, blank=True, null=True)
#     商品序号 = models.CharField(max_length=255, blank=True, null=True)
#     商品编号 = models.CharField(max_length=255, blank=True, null=True)
#     商品名称 = models.CharField(max_length=255, blank=True, null=True)
#     商品规格型号 = models.CharField(max_length=255, blank=True, null=True)
#     第一法定计量单位 = models.CharField(max_length=255, blank=True, null=True)
#     申报日期 = models.CharField(max_length=255, blank=True, null=True)
#     实征从价关税率 = models.CharField(max_length=255, blank=True, null=True)
#     应征从价关税率 = models.CharField(max_length=255, blank=True, null=True)
#     每项商品需要监管证件 = models.CharField(max_length=255, blank=True, null=True)
#     产销国 = models.CharField(max_length=255, blank=True, null=True)
#     经营单位编号 = models.CharField(max_length=255, blank=True, null=True)
#     经营单位名称 = models.CharField(max_length=255, blank=True, null=True)
#     货主单位代码 = models.CharField(max_length=255, blank=True, null=True)
#     货主单位名称 = models.CharField(max_length=255, blank=True, null=True)
#     申报单位代码 = models.CharField(max_length=255, blank=True, null=True)
#     申报单位名称 = models.CharField(max_length=255, blank=True, null=True)
#     监管方式 = models.CharField(max_length=255, blank=True, null=True)
#     实征从量关税税率 = models.CharField(max_length=255, blank=True, null=True)
#     应征从量关税税率 = models.CharField(max_length=255, blank=True, null=True)
#     实征从价增值税率 = models.CharField(max_length=255, blank=True, null=True)
#     应征从价增值税率 = models.CharField(max_length=255, blank=True, null=True)
#     实征从价消费税率 = models.CharField(max_length=255, blank=True, null=True)
#     应征从价消费税率 = models.CharField(max_length=255, blank=True, null=True)
#     实征从量消费税税率 = models.CharField(max_length=255, blank=True, null=True)
#     应征从量消费税税率 = models.CharField(max_length=255, blank=True, null=True)
#     实征从价反倾销税税率 = models.CharField(max_length=255, blank=True, null=True)
#     应征从价反倾销税税率 = models.CharField(max_length=255, blank=True, null=True)
#     关税完税价 = models.CharField(max_length=255, blank=True, null=True)
#     第一法定数量 = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'data1'


class Data2(models.Model):
    customs_id = models.CharField(max_length=50, blank=True, null=True)
    product_number = models.CharField(max_length=50, blank=True, null=True)
    product_id = models.CharField(max_length=50, blank=True, null=True)
    elements = models.CharField(max_length=255, blank=True, null=True)
    text_elements = models.TextField(blank=True, null=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'data2'


class Datax(models.Model):
    id = models.BigAutoField(primary_key=True)
    customs_id = models.CharField(max_length=50, blank=True, null=True, verbose_name="海关编号")
    product_number = models.CharField(max_length=50, blank=True, null=True, verbose_name="商品序号")
    product_id = models.CharField(max_length=255, blank=True, null=True, verbose_name="商品编号")
    product_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="商品名称")
    guige = models.CharField(max_length=255, blank=True, null=True, verbose_name="规格型号")
    diyi_jiliang = models.CharField(max_length=255, blank=True, null=True)
    shenbao_date = models.CharField(max_length=255, blank=True, null=True)
    shi_jia_guan = models.CharField(max_length=255, blank=True, null=True)
    ying_jia_guan = models.CharField(max_length=255, blank=True, null=True)
    jian_zhengjian = models.CharField(max_length=255, blank=True, null=True)
    chanxiaoguo = models.CharField(max_length=255, blank=True, null=True)
    jingying_code = models.CharField(max_length=255, blank=True, null=True)
    jingying_name = models.CharField(max_length=255, blank=True, null=True)
    huozhu_code = models.CharField(max_length=255, blank=True, null=True)
    huozhu_name = models.CharField(max_length=255, blank=True, null=True)
    shenbao_code = models.CharField(max_length=255, blank=True, null=True)
    shenbao_name = models.CharField(max_length=255, blank=True, null=True)
    jian_style = models.CharField(max_length=255, blank=True, null=True)
    shi_liang_guan = models.CharField(max_length=255, blank=True, null=True)
    ying_liang_guan = models.CharField(max_length=255, blank=True, null=True)
    shi_jia_zeng = models.CharField(max_length=255, blank=True, null=True)
    ying_jia_zeng = models.CharField(max_length=255, blank=True, null=True)
    shi_jia_xiao = models.CharField(max_length=255, blank=True, null=True)
    ying_jia_xiao = models.CharField(max_length=255, blank=True, null=True)
    shi_liang_xiao = models.CharField(max_length=255, blank=True, null=True)
    ying_liang_xiao = models.CharField(max_length=255, blank=True, null=True)
    shi_jia_fan = models.CharField(max_length=255, blank=True, null=True)
    ying_jia_fan = models.CharField(max_length=255, blank=True, null=True)
    shui_jia = models.CharField(max_length=255, blank=True, null=True)
    diyi_shuliang = models.CharField(max_length=255, blank=True, null=True)
    tag = models.IntegerField(verbose_name="是否为风险税率")

    class Meta:
        managed = False
        db_table = 'datax'


class Dataxx(Datax):
    tag_label = models.BooleanField(blank=True, null=True)

    def name(self, tag):
        self.tag_label = tag


class DirectoryFactorRel(models.Model):
    uid = models.BigAutoField(primary_key=True)
    product_code = models.ForeignKey('TDirectoryCode', models.DO_NOTHING, db_column='product_code')
    element_code = models.ForeignKey('TFactorCode', models.DO_NOTHING, db_column='element_code')
    enable = models.BooleanField(blank=True, null=True)
    enable_test = models.BooleanField(blank=True, null=True)
    enable_key = models.BooleanField(blank=True, null=True)
    enabletime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    keywords = models.CharField(max_length=50, blank=True, null=True)
    crisis = models.FloatField(blank=True, null=True)
    wrongwords = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'directory_factor_rel'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class TCodingRules(models.Model):
    element_id = models.CharField(primary_key=True, max_length=50)
    element_name = models.CharField(max_length=50, blank=True, null=True)
    enable_small_alp = models.IntegerField()
    enable_big_alp = models.IntegerField(blank=True, null=True)
    enable_figure = models.IntegerField()
    length = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_coding_rules'


class TDirectoryCode(models.Model):
    product_code = models.CharField(primary_key=True, max_length=50)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    enable_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    whether_enable = models.BooleanField(db_column='Whether_enable', blank=True,
                                         null=True)  # Field name made lowercase.
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_directory_code'


class TFactorCode(models.Model):
    element_code = models.CharField(primary_key=True, max_length=50)
    element_name = models.CharField(max_length=255)
    # element_uid = models.AutoField()
    syno_code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_factor_code'


class WmdThresholdValue(models.Model):
    element_code = models.CharField(max_length=50)
    value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'wmd_threshold_value'
