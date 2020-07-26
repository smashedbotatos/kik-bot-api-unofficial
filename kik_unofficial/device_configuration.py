"""
Here we put all the device configuration that we emulate.
"""

# possible kik versions to emulate
kik_version_11_info = {"kik_version": "11.1.1.12218", "classes_dex_sha1_digest": "aCDhFLsmALSyhwi007tvowZkUd0="}
kik_version_13_info = {"kik_version": "13.4.0.9614", "classes_dex_sha1_digest": "ETo70PFW30/jeFMKKY+CNanX2Fg="}
kik_version_14_info = {"kik_version": "14.0.0.11130", "classes_dex_sha1_digest": "9nPRnohIOTbby7wU1+IVDqDmQiQ="}
kik_version_14_5_info = {"kik_version": "14.5.0.13136", "classes_dex_sha1_digest": "LuYEjtvBu4mG2kBBG0wA3Ki1PSE="}
kik_version_15_21_info = {'kik_version': '15.21.0.22201', 'classes_dex_sha1_digest': 'MbZ+Zbjaz5uFXKFDM88CwFh7DAg='}
kik_version_15_26_info = {'kik_version': '15.26.1.22599', 'classes_dex_sha1_digest': 'FufnfECcxD6i8ImvzMoaCPPIcTU='}

device_id = "43cc483c7a98fe685fa94ab078a8638c"  # random 16 bytes. Generate once and don't change
# https://www.random.org/bytes/
kik_version_info = kik_version_15_26_info  # a kik version that's not updated might cause a captcha on login
android_id = "4105264f46d4a986"  # random 8 bytes. Generate once and don't change https://www.random.org/bytes/

# Change info given to kik on login request. To help from looking suspicious.
operator = "310260"  # Carrier code, set for a Carrier that is in your county. https://www.imei.info/carriers/
brand = "samsung"  # Phone Brand, set a brand that matches your model.
model = "Samsung Galaxy S7 edge"  # Phone Model Name Sting - Find a model name https://browser.geekbench.com/v5/cpu
android_sdk = "26"  # Match SDK to Android OS version of the Model -
# https://developer.android.com/studio/releases/platforms
install_date = "1570976775000"  # App Install Date - Epoch Time - https://www.epochconverter.com
logins_since_install = "6"  # Kik Logins since App install - Randomize this a number between 1 and 15
registrations_since_install = "3"  # Account Registrations since app install. Randomize this number between 1 and 5
