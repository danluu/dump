(when (>= emacs-major-version 24)
  (require 'package)
  (add-to-list
   'package-archives
   '("melpa" . "http://melpa.org/packages/")
   t)
    (package-initialize))

(setq make-backup-files nil)
(setq-default indent-tabs-mode nil)
(setq-default c-basic-offset 4)
(setq c-basic-offset 4)
(setq c-indent-level 4)
(setq tab-width 4)

(add-hook 'before-save-hook 'delete-trailing-whitespace)
(setq-default fill-column 80)
