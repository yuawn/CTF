#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/fs.h>
#include <linux/proc_fs.h>
#include <linux/string.h>
#include <linux/slab.h>
#include <asm/uaccess.h>
#include <linux/uaccess.h>
#define MAX_NOTE 8

static DEFINE_MUTEX(lock);

struct note {
  unsigned long size;
  char *contents;
};

unsigned long cnt;
unsigned long selected;
struct note notes[MAX_NOTE];


ssize_t gnote_write(struct file *filp, const char __user *buf, size_t count, loff_t *f_pos)
{
  unsigned int index;
  mutex_lock(&lock);
  /*
   * 1. add note
   * 2. edit note
   * 3. delete note
   * 4. copy note
   * 5. select note
   * No implementation :(
   */
  switch(*(unsigned int *)buf){
    case 1:
      if(cnt >= MAX_NOTE){
        break;
      }
      notes[cnt].size = *((unsigned int *)buf+1);
      if(notes[cnt].size > 0x10000){
        break;
      }
      notes[cnt].contents = kmalloc(notes[cnt].size, GFP_KERNEL);
      cnt++;
      break;
    case 2:
      printk("Edit Not implemented\n");
      break;
    case 3:
      printk("Delete Not implemented\n");
      break;
    case 4:
      printk("Copy Not implemented\n");
      break;
    case 5:
      index = *((unsigned int *)buf+1);
      if(cnt > index){
        selected = index;
      }
      break;
  }
  mutex_unlock(&lock);
  return count;
}

ssize_t gnote_read(struct file *filp, char __user *buf, size_t count, loff_t *f_pos)
{
  mutex_lock(&lock);
  if(selected == -1){
    mutex_unlock(&lock);
    return 0;
  }
  if(count > notes[selected].size){
    count = notes[selected].size;
  }
  copy_to_user(buf, notes[selected].contents, count);
  selected = -1;
  mutex_unlock(&lock);
  return count;
}

struct file_operations gnote_proc = {
  .write    = gnote_write,
  .read    = gnote_read,
};

static int __init gnote_init(void)
{
  cnt=0;
  selected=-1;
  proc_create_data("gnote", 0666, NULL, &gnote_proc, NULL);
  printk("/proc/gnote created\n");
  return 0;
}
 
static void __exit
gnote_exit(void)
{
  remove_proc_entry("gnote", NULL);
  printk("unloading gnote\n");
}
 
module_init(gnote_init);
module_exit(gnote_exit);
