# Generated by Django 4.2.3 on 2024-03-31 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_category_options_alter_color_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
        migrations.AlterField(
            model_name='property',
            name='color',
            field=models.CharField(choices=[('سفید', 'سفید'), ('مشکی', 'مشکی'), ('قهوه\u200cای', 'قهوه\u200cای'), ('قرمز', 'قرمز'), ('زرد', 'زرد'), ('سبز', 'سبز'), ('آبی', 'آبی'), ('سرخابی', 'سرخابی'), ('صورتی', 'صورتی'), ('بنفش', 'بنفش'), ('نارنجی', 'نارنجی'), ('خاکستری', 'خاکستری'), ('نیلی', 'نیلی'), ('زرشکی', 'زرشکی'), ('نقره\u200cای', 'نقره\u200cای'), ('طلایی', 'طلایی'), ('بژ', 'بژ'), ('زیتونی', 'زیتونی'), ('خاکستری-آبی', 'خاکستری-آبی'), ('یشمی', 'یشمی'), ('سبز دریایی', 'سبز دریایی'), ('زعفرانی', 'زعفرانی'), ('بادمجانی', 'بادمجانی'), ('خرمایی', 'خرمایی'), ('خردلی', 'خردلی'), ('نخودی', 'نخودی'), ('هلویی', 'هلویی'), ('لیمویی', 'لیمویی'), ('آلبالوئی', 'آلبالوئی'), ('شنی', 'شنی'), ('اسموتی', 'اسموتی'), ('مرجانی', 'مرجانی'), ('سپید', 'سپید'), ('کرم', 'کرم'), ('زرشکی روشن', 'زرشکی روشن'), ('قرمز شدید', 'قرمز شدید'), ('آبی کمرنگ', 'آبی کمرنگ'), ('بنفش آبی', 'بنفش آبی'), ('سبز نارنجی', 'سبز نارنجی'), ('سرخابی', 'سرخابی'), ('خاکستری تیره', 'خاکستری تیره'), ('سبز کبریتی', 'سبز کبریتی'), ('سیاه تیره', 'سیاه تیره'), ('آبی سیر', 'آبی سیر'), ('زرد آفتابی', 'زرد آفتابی'), ('صورتی شیرین', 'صورتی شیرین'), ('خرمایی روشن', 'خرمایی روشن'), ('سفید براق', 'سفید براق'), ('آبی روشن', 'آبی روشن'), ('سبز زمردی', 'سبز زمردی'), ('قرمز قوی', 'قرمز قوی'), ('صورتی سیر', 'صورتی سیر'), ('سیاه مات', 'سیاه مات'), ('سرخابی روشن', 'سرخابی روشن'), ('زیتونی تیره', 'زیتونی تیره'), ('قهوه ایست', 'قهوه ایست'), ('زرد کرفسی', 'زرد کرفسی'), ('فیروزه ای', 'فیروزه ای'), ('سبک یشمی', 'سبک یشمی'), ('نارنجی مات', 'نارنجی مات'), ('صورتی مات', 'صورتی مات'), ('سبز کاکتوسی', 'سبز کاکتوسی'), ('سبز زمردی', 'سبز زمردی'), ('نیلی مات', 'نیلی مات'), ('صورتی تیره', 'صورتی تیره'), ('سبز آووکادو', 'سبز آووکادو'), ('آمبر', 'آمبر'), ('بادمجانی تیره', 'بادمجانی تیره'), ('آلبالوئی تیره', 'آلبالوئی تیره'), ('خرمایی مات', 'خرمایی مات'), ('زرد گندمی', 'زرد گندمی'), ('آبی سمت', 'آبی سمت'), ('صورتی مایل', 'صورتی مایل'), ('سنگی', 'سنگی'), ('سرخس', 'سرخس'), ('نارنجی روشن', 'نارنجی روشن'), ('خاکستری مات', 'خاکستری مات'), ('سفید کاکتوسی', 'سفید کاکتوسی'), ('سبز تیره', 'سبز تیره'), ('آبی روشن', 'آبی روشن'), ('آبی اقیانوسی', 'آبی اقیانوسی'), ('سبز آبی', 'سبز آبی'), ('آبی تاریک', 'آبی تاریک'), ('صورتی روشن', 'صورتی روشن'), ('قهوه\u200cای تیره', 'قهوه\u200cای تیره'), ('قرمز تیره', 'قرمز تیره'), ('سبز زیتونی', 'سبز زیتونی'), ('طلایی تیره', 'طلایی تیره'), ('زرد لیمویی', 'زرد لیمویی'), ('سرخسی', 'سرخسی'), ('آلبالوئی شیرین', 'آلبالوئی شیرین'), ('سفید سنگی', 'سفید سنگی'), ('خاکستری آهکی', 'خاکستری آهکی'), ('خاکستری سرمه\u200cای', 'خاکستری سرمه\u200cای'), ('قهوه\u200cای مایل', 'قهوه\u200cای مایل'), ('مشگی', 'مشگی'), ('قرمز گندمی', 'قرمز گندمی'), ('سیاه شکوفه', 'سیاه شکوفه'), ('آبی مات', 'آبی مات'), ('صورتی گلابی', 'صورتی گلابی'), ('سبز لیمویی', 'سبز لیمویی'), ('سبز ترشو', 'سبز ترشو'), ('بنفش نیمه تیره', 'بنفش نیمه تیره'), ('نیلی عمیق', 'نیلی عمیق'), ('مشکی خاکی', 'مشکی خاکی'), ('صورتی نیمه تیره', 'صورتی نیمه تیره'), ('آبی لاجوردی', 'آبی لاجوردی'), ('خاکستری روشن', 'خاکستری روشن'), ('سبز دریایی روشن', 'سبز دریایی روشن'), ('زرد شنی', 'زرد شنی'), ('آبی ملانژ', 'آبی ملانژ'), ('نارنجی ملانژ', 'نارنجی ملانژ'), ('سبز شاه\u200cبلوطی', 'سبز شاه\u200cبلوطی'), ('قهوه\u200cای سوخته', 'قهوه\u200cای سوخته'), ('کرم موزائیکی', 'کرم موزائیکی'), ('سبز بادمجانی', 'سبز بادمجانی'), ('صورتی لیمویی', 'صورتی لیمویی'), ('زرشکی چینی', 'زرشکی چینی'), ('نارنجی روشن', 'نارنجی روشن'), ('سبز چمنی', 'سبز چمنی'), ('قرمز آتشین', 'قرمز آتشین'), ('آبی مالون', 'آبی مالون'), ('صورتی نیلوفری', 'صورتی نیلوفری'), ('سبز کاغذی', 'سبز کاغذی'), ('آبی آسمانی', 'آبی آسمانی'), ('صورتی صدفی', 'صورتی صدفی'), ('آبی شاهتوت', 'آبی شاهتوت'), ('صورتی گلابی', 'صورتی گلابی'), ('زرد آهکی', 'زرد آهکی'), ('مشکی باز', 'مشکی باز'), ('صورتی آویزان', 'صورتی آویزان'), ('آبی باز', 'آبی باز'), ('سبز آویزان', 'سبز آویزان'), ('قرمز آویزان', 'قرمز آویزان'), ('صورتی مات', 'صورتی مات'), ('سبز مات', 'سبز مات'), ('آبی مات', 'آبی مات'), ('زرد مات', 'زرد مات'), ('نارنجی مات', 'نارنجی مات'), ('قرمز مات', 'قرمز مات'), ('سفید مات', 'سفید مات'), ('مشکی مات', 'مشکی مات'), ('خاکستری مات', 'خاکستری مات'), ('کرم مات', 'کرم مات'), ('سبز نوشیدنی', 'سبز نوشیدنی'), ('قهوه\u200cای نوشیدنی', 'قهوه\u200cای نوشیدنی'), ('لیمویی نوشیدنی', 'لیمویی نوشیدنی'), ('صورتی نوشیدنی', 'صورتی نوشیدنی'), ('آبی نوشیدنی', 'آبی نوشیدنی'), ('زرد نوشیدنی', 'زرد نوشیدنی'), ('قرمز نوشیدنی', 'قرمز نوشیدنی'), ('نیلی نوشیدنی', 'نیلی نوشیدنی'), ('سفید نوشیدنی', 'سفید نوشیدنی'), ('مشکی نوشیدنی', 'مشکی نوشیدنی'), ('سرخابی نوشیدنی', 'سرخابی نوشیدنی'), ('کرم نوشیدنی', 'کرم نوشیدنی'), ('بادمجانی نوشیدنی', 'بادمجانی نوشیدنی'), ('صورتی نوشیدنی', 'صورتی نوشیدنی'), ('سبز نارنجی نوشیدنی', 'سبز نارنجی نوشیدنی'), ('قهوه\u200cای نوشیدنی', 'قهوه\u200cای نوشیدنی'), ('زرشکی نوشیدنی', 'زرشکی نوشیدنی'), ('زرد آبی نوشیدنی', 'زرد آبی نوشیدنی'), ('قرمز آبی نوشیدنی', 'قرمز آبی نوشیدنی'), ('قرمز سبز نوشیدنی', 'قرمز سبز نوشیدنی'), ('آبی توت', 'آبی توت'), ('سبز زیتونی مات', 'سبز زیتونی مات'), ('زرد خردلی', 'زرد خردلی'), ('سبز کهربایی', 'سبز کهربایی'), ('صورتی فلامینگو', 'صورتی فلامینگو'), ('صورتی گوجه\u200cفرنگی', 'صورتی گوجه\u200cفرنگی'), ('آبی اتریشی', 'آبی اتریشی'), ('سبز الغر', 'سبز الغر'), ('قرمز لاکپشتی', 'قرمز لاکپشتی'), ('آبی رعد و برق', 'آبی رعد و برق'), ('سبز آتشی', 'سبز آتشی'), ('صورتی ارکید', 'صورتی ارکید'), ('قهوه\u200cای کارامل', 'قهوه\u200cای کارامل'), ('آبی اقیانوس', 'آبی اقیانوس'), ('سفید انبار', 'سفید انبار'), ('سبز جاده', 'سبز جاده'), ('نارنجی دارابی', 'نارنجی دارابی'), ('زرشکی راش', 'زرشکی راش'), ('سبز پنبه\u200cای', 'سبز پنبه\u200cای'), ('صورتی بابانوئل', 'صورتی بابانوئل'), ('سبز مارمولکی', 'سبز مارمولکی'), ('آبی کوشکی', 'آبی کوشکی'), ('زرشکی گیلاسی', 'زرشکی گیلاسی'), ('سبز گیلاسی', 'سبز گیلاسی'), ('قرمز دمسی', 'قرمز دمسی'), ('آبی نافیسی', 'آبی نافیسی'), ('صورتی کوسه\u200cای', 'صورتی کوسه\u200cای'), ('سبز چتری', 'سبز چتری'), ('قرمز خوشه\u200cای', 'قرمز خوشه\u200cای'), ('زرد خامی', 'زرد خامی'), ('قهوه\u200cای موبر', 'قهوه\u200cای موبر'), ('سبز شاه\u200cتوتی', 'سبز شاه\u200cتوتی'), ('آبی شاهین\u200cتختی', 'آبی شاهین\u200cتختی'), ('صورتی شهوانی', 'صورتی شهوانی'), ('سبز شمشادی', 'سبز شمشادی'), ('قرمز برگ\u200cپیچان', 'قرمز برگ\u200cپیچان'), ('آبی دلارامی', 'آبی دلارامی'), ('صورتی پیازی', 'صورتی پیازی'), ('قهوه\u200cای کدر', 'قهوه\u200cای کدر'), ('آبی آتشی', 'آبی آتشی'), ('زرد گلابی', 'زرد گلابی'), ('صورتی ریواسی', 'صورتی ریواسی'), ('سبز لگویی', 'سبز لگویی'), ('قرمز باسی', 'قرمز باسی'), ('آبی توریالی', 'آبی توریالی'), ('زرد خاکستری', 'زرد خاکستری'), ('صورتی پرتقالی', 'صورتی پرتقالی'), ('آبی الواسی', 'آبی الواسی'), ('سبز پروانه\u200cای', 'سبز پروانه\u200cای'), ('صورتی کاغذی', 'صورتی کاغذی'), ('آبی ارگنونی', 'آبی ارگنونی'), ('سبز قدسی', 'سبز قدسی'), ('قرمز تابستانی', 'قرمز تابستانی'), ('آبی هوایی', 'آبی هوایی'), ('صورتی حنایی', 'صورتی حنایی'), ('آبی سماقی', 'آبی سماقی'), ('زرد سربی', 'زرد سربی'), ('سبز کوهی', 'سبز کوهی'), ('قهوه\u200cای بنفش', 'قهوه\u200cای بنفش'), ('صورتی خیامی', 'صورتی خیامی'), ('آبی حکمتی', 'آبی حکمتی'), ('سبز حیوانی', 'سبز حیوانی'), ('صورتی غنچه\u200cای', 'صورتی غنچه\u200cای'), ('بنفش مایل', 'بنفش مایل'), ('سبز پوشالی', 'سبز پوشالی'), ('قرمز تند', 'قرمز تند'), ('آبی سحرآمیز', 'آبی سحرآمیز'), ('صورتی کاندید', 'صورتی کاندید'), ('زرشکی رسن', 'زرشکی رسن'), ('سبز درخشان', 'سبز درخشان'), ('آبی جویباری', 'آبی جویباری'), ('صورتی سرخابی', 'صورتی سرخابی'), ('سبز گوشه\u200cای', 'سبز گوشه\u200cای'), ('قهوه\u200cای موریتانی', 'قهوه\u200cای موریتانی'), ('آبی شاکری', 'آبی شاکری'), ('صورتی گلگون', 'صورتی گلگون'), ('زرشکی خیابانی', 'زرشکی خیابانی'), ('سبز فیروزه\u200cای', 'سبز فیروزه\u200cای'), ('قرمز طلایی', 'قرمز طلایی'), ('آبی شمالی', 'آبی شمالی'), ('صورتی طوسی', 'صورتی طوسی'), ('سبز زمردی', 'سبز زمردی'), ('قهوه\u200cای محمدی', 'قهوه\u200cای محمدی'), ('آبی تجدیدپذیر', 'آبی تجدیدپذیر')], default=' ', max_length=90, verbose_name='color'),
        ),
        migrations.AlterField(
            model_name='property',
            name='size',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('2XL', '2X'), ('3XL', '3XL'), ('4XL', '4XL'), ('5XL', '5XL'), ('30', '30'), ('31', '31'), ('32', '32'), ('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44'), ('45', '45'), ('46', '46'), ('36', '36'), ('47', '47'), ('48', '48'), ('49', '49'), ('48', '48'), ('49', '49'), ('50', '50')], max_length=10, verbose_name='size'),
        ),
    ]
