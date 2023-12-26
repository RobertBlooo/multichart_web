from django.db import models

class Session(models.Model):
    name = models.CharField(max_length=5, verbose_name='交易時段')
    trade_time = models.CharField(max_length=20, default=' ', verbose_name='交易時間')
    def __str__(self):
        return self.name
    
class Commodity(models.Model):
    commodity_id = models.CharField(max_length=10, verbose_name='交易商品ID')
    name = models.CharField(max_length=10, verbose_name='交易商品名稱')
    point_value = models.PositiveIntegerField(default=200, verbose_name='一點的價格')
    def __str__(self):
        return self.name

class Strategy(models.Model):
    strategy_id = models.CharField(max_length=10, verbose_name='策略ID')
    name = models.CharField(max_length=10, help_text="最多10字元", verbose_name='策略名稱')
    session = models.ForeignKey(Session, blank=False, on_delete=models.CASCADE, verbose_name='交易時段')
    commodity = models.ForeignKey(Commodity, blank=False, on_delete=models.CASCADE, verbose_name='交易商品')
    profit = models.PositiveIntegerField(verbose_name='淨獲利')
    profit_factor = models.FloatField(verbose_name='獲利因子')
    mdd = models.IntegerField(verbose_name='最大策略回測')
    hazard_ratio = models.FloatField(verbose_name='風報比')
    nums_trade = models.PositiveIntegerField(verbose_name='交易次數')
    continue_loss = models.PositiveIntegerField(verbose_name='連續策略虧損次數')
    settlement = models.BooleanField(default=True, verbose_name='參加結算與否')
    body = models.TextField(max_length=2000, default=" tell something", verbose_name='策略描述')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='填寫日期')
    
    class Meta:
        ordering = ('-pub_date',)
    
    def __str__(self):
        return self.name

class PPhoto(models.Model):
    name = models.CharField(max_length=20, default='', verbose_name='圖片名稱')
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE, verbose_name='策略名稱')
    url = models.URLField(default='', max_length=5000)
    

    def __str__(self):
        return self.name