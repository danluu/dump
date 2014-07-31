################################################################################
#
# sigsegv
#
################################################################################

SIGSEGV_VERSION = 1.0.02
SIGSEGV_SOURCE = sigsegv-$(SIGSEGV_VERSION).src.tar.gz
SIGSEGV_SITE = /home/dluu/dev/dump/sigsegv/
SIGSEGV_SITE_METHOD = local
SIGSEGV_INSTALL_STAGING = YES
SIGSEGV_BINARY = sigsegv
SIGSEGV_DEPENDENCIES =
SIGSEGV_CONF_OPT =
SIGSEGV_LICENSE = GPLv2+ (programs), LGPLv2.1+ (libraries)
SIGSEGV_LICENSE_FILES = COPYING

define LIBSIGSEGV_BUILD_CMDS
	$(MAKE) CC="$(TARGET_CC)" LD="$(TARGET_LD)" -C -g $(@D) all
endef

define SIGSEGV_INSTALL_TARGET_CMDS
        $(INSTALL) -D -m 0755 $(@D)/sigsegv $(TARGET_DIR)/bin
endef

define SIGSEGV_PERMISSIONS
       /bin/sigsegv f 4755 0 0 - - - - - 
endef

$(eval $(generic-package))
