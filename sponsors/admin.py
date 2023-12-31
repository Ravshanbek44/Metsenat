from django.contrib import admin

from sponsors.models import SponsorWallet


class SponsorWalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'sponsor', 'sponsor_wallet', 'spent_amounts', 'wallet_avg')


admin.site.register(SponsorWallet, SponsorWalletAdmin)
