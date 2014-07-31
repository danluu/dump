Simple binary that segfaults plus extra files for buildroot build. Put the files in buildroot in buildroot's package/sigsegv/ directory and then modify the package/Config.in to add this package.

This was used to figure out what linux does on a segfault by running it under qemu and attaching to qemu with gdb.

[The instructions here](http://www.linux-magazine.com/Online/Features/Qemu-and-the-Kernel) mostly work, with some minor modifications. They're on an older version of buildroot, so the "Compile the kernel with debug info" isn't where it's shown in the screenshot, but it's possible to search for it with `/`.

They recommend running `qemu -kernel output/images/bzImage -hda output/images/rootfs.ext2 -append "root=/dev/sda rw" -s -S`, but attaching to a qemu with `-S` confuses gdb since the architecture changes when the image starts up. Also, `qemu` needs to be aliased to `qemu-system-footarget`.
