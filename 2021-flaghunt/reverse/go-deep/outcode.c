void _init()
{
    if (__gmon_start__ != 0)
    {
        __gmon_start__();
    }
}

void std::allocator<char>::~allocator(class std::allocator<char> *const this)
{
    /* tailcall */
    return std::allocator<char>::~allocator(this);
}

int64_t sub_2036()
{
    int64_t var_8 = 0;
    int64_t var_10 = data_5008;
    /* jump -> data_5010 */
}

void *__cxa_begin_catch(void *exceptionObject)
{
    /* tailcall */
    return __cxa_begin_catch(exceptionObject);
}

void std::string::string(class std::string *const this)
{
    /* tailcall */
    return std::string::string(this);
}

uint64_t strlen(char const *arg1)
{
    /* tailcall */
    return strlen(arg1);
}

void std::string::~string(class std::string *const this)
{
    /* tailcall */
    return std::string::~string(this);
}

void std::string::_M_set_length(class std::string *const this,
                                std::string::size_type __n)
{
    /* tailcall */
    return std::string::_M_set_length(this, __n);
}

int64_t std::__throw_logic_error(char const *arg1)
{
    /* tailcall */
    return std::__throw_logic_error(arg1);
}

std::string::pointer std::string::_M_local_data(class std::string *const this)
{
    /* tailcall */
    return std::string::_M_local_data(this);
}

void std::string::_M_data(class std::string *const this,
                          std::string::pointer __p)
{
    /* tailcall */
    return std::string::_M_data(this, __p);
}

int32_t __cxa_atexit(void (*func)(void *), void *arg, void *dso_handle)
{
    /* tailcall */
    return __cxa_atexit(func, arg, dso_handle);
}

class std::ostream &std::operator<< <std::char_traits<char>>(
    class std::ostream &__out, char const *__s)
{
    /* tailcall */
    return std::operator<< <std::char_traits<char>>(__out, __s);
}

std::ostream::__ostream_type *std::ostream::operator<<(
    class std::ostream *const this,
    std::ostream::__ostream_type &(*__pf)(std::ostream::__ostream_type &))
{
    /* tailcall */
    return std::ostream::operator<<(this, __pf);
}

void std::string::_Alloc_hider::_Alloc_hider(
    struct std::string::_Alloc_hider *const this, std::string::pointer __dat)
{
    /* tailcall */
    return std::string::_Alloc_hider::_Alloc_hider(this, __dat);
}

void std::allocator<char>::~allocator(class std::allocator<char> *const this)
{
    /* tailcall */
    return std::allocator<char>::~allocator(this);
}

std::string::pointer std::string::_M_data(class std::string *const this)
{
    /* tailcall */
    return std::string::_M_data(this);
}

void std::string::_S_copy_chars(char *__p, char const *__k1, char const *__k2)
{
    /* tailcall */
    return std::string::_S_copy_chars(__p, __k1, __k2);
}

class std::string *const std::string::operator=(class std::string *const this,
                                                class std::string &__str)
{
    /* tailcall */
    return std::string::operator=(this, __str);
}

void std::string::_M_dispose(class std::string *const this)
{
    /* tailcall */
    return std::string::_M_dispose(this);
}

class std::istream &
std::operator>><char, std::char_traits<char>, std::allocator<char>>(
    class std::istream &__in, class std::string &__str)
{
    /* tailcall */
    return std::operator>><char, std::char_traits<char>, std::allocator<char>>(__in, __str);
}

void std::string::string(class std::string *const this)
{
    /* tailcall */
    return std::string::string(this);
}

void __cxa_rethrow() __noreturn
{
    /* tailcall */
    return __cxa_rethrow();
}

std::string::size_type std::string::length(class std::string *const this)
{
    /* tailcall */
    return std::string::length(this);
}

void std::ios_base::Init::Init(class std::ios_base::Init *const this)
{
    /* tailcall */
    return std::ios_base::Init::Init(this);
}

void __cxa_end_catch()
{
    /* tailcall */
    return __cxa_end_catch();
}

void _Unwind_Resume(struct _Unwind_Exception *exc)
{
    /* tailcall */
    return _Unwind_Resume(exc);
}

void std::allocator<char>::allocator(class std::allocator<char> *const this)
{
    /* tailcall */
    return std::allocator<char>::allocator(this);
}

std::string::pointer std::string::_M_create(class std::string *const this,
                                            std::string::size_type &__capacity, std::string::size_type __old_capacity)
{
    /* tailcall */
    return std::string::_M_create(this, __capacity, __old_capacity);
}

void std::string::_M_capacity(class std::string *const this,
                              std::string::size_type __capacity)
{
    /* tailcall */
    return std::string::_M_capacity(this, __capacity);
}

std::string::reference std::string::operator[](class std::string *const this,
                                               std::string::size_type __pos)
{
    /* tailcall */
    return std::string::operator[](this, __pos);
}

void __cxa_finalize(void *d)
{
    /* tailcall */
    return __cxa_finalize(d);
}

int64_t _start(int64_t arg1, int64_t arg2, void (*arg3)()) __noreturn
{
    int64_t rax;
    int64_t var_8 = rax;
    __libc_start_main(main, __return_addr, &arg_8, nullptr, nullptr, arg3, &var_8);
    /* no return */
}

void deregister_tm_clones()
{
    return;
}

void register_tm_clones()
{
    return;
}

void __do_global_dtors_aux()
{
    if (completed .0 != 0)
    {
        return;
    }
    if (__cxa_finalize != 0)
    {
        __cxa_finalize(__dso_handle);
    }
    deregister_tm_clones();
    completed .0 = 1;
}

int64_t frame_dummy()
{
    /* tailcall */
    return register_tm_clones();
}

class std::string *magic(class std::string *arg1, class std::string *arg2,
                         class std::string *arg3)
{
    std::string::string(arg1);
    std::string::size_type rax_2 = std::string::length(arg3);
    std::string::size_type rax_4 = std::string::length(arg2);
    std::string::size_type var_20 = 0;
    for (std::string::size_type var_28 = 0; var_28 < rax_4; var_28 = (var_28 + 1))
    {
        value_type rbx_2 = (*(int8_t *)std::string::operator[](arg2, var_28) ^ *(int8_t *)std::string::operator[](arg3, var_20));
        *(int8_t *)std::string::operator[](arg1, var_28) = rbx_2;
        std::string::size_type var_20_1 = (var_20 + 1);
        std::string::size_type rax_13;
        if (var_20_1 >= rax_2)
        {
            rax_13 = 0;
        }
        else
        {
            rax_13 = var_20_1;
        }
        var_20 = rax_13;
    }
    return arg1;
}

int32_t main(int32_t argc, char **argv, char **envp)
{
    int32_t var_f8 = 0x10;
    int32_t var_f4 = 0x30;
    int32_t var_f0 = 0x25;
    int32_t var_ec = 0x30;
    int32_t var_e8 = 0x21;
    int32_t var_e4 = 0x4e;
    int32_t var_e0 = 0xc;
    int32_t var_dc = 0x62;
    int32_t var_d8 = 0x19;
    int32_t var_d4 = 0x44;
    int32_t var_d0 = 0x5d;
    int32_t var_cc = 0x3d;
    int32_t var_c8 = 0x38;
    int32_t var_c4 = 1;
    int32_t var_c0 = 0x54;
    int32_t var_bc = 0x15;
    int32_t var_b8 = 0x2d;
    int32_t var_b4 = 0x26;
    int32_t var_b0 = 0x1c;
    int32_t var_ac = 0x3e;
    int32_t var_a8 = 0x3f;
    int32_t var_a4 = 0x18;
    int32_t var_a0 = 7;
    int32_t var_9c = 0x5f;
    int32_t var_98 = 9;
    int32_t var_94 = 0x54;
    int32_t var_90 = 0x2e;
    void var_118;
    std::string::string(&var_118);
    void var_138;
    std::string::string(&var_138);
    int32_t var_f4_1 = 0x67;
    int32_t var_e4_1 = 0xf;
    int32_t var_cc_1 = 0x5d;
    int32_t var_c0_1 = 0;
    std::operator<< <std::char_traits<char>>(&std::cout, "Give us any data, We will xor it…");
    std::operator>><char, st... _traits<char>, std::allocator<char>>(&std::cin, &var_118);
    void var_39;
    std::allocator<char>::allocator(&var_39);
    void var_68;
    std::string::string<std::allocator<char>>(&var_68, "S3cret_St41ng");
    void var_38;
    std::string::string(&var_38);
    void var_88;
    magic(&var_88, &var_38, &var_68);
    std::string::operator=(&var_138, &var_88);
    std::string::~string(&var_88);
    std::string::~string(&var_38);
    std::string::~string(&var_68);
    std::allocator<char>::~allocator(&var_39);
    std::ostream::operator<<(std::operator<< <std::char_traits<char>>(&std::cout, "Go Deep!"), std::endl<char>);
    std::string::~string(&var_138);
    std::string::~string(&var_118);
    return 0;
}

int64_t sub_2666(struct _Unwind_Exception *arg1 @rax, void *arg2 @rbp)
{
    std::string::~string(((char *)arg2 - 0x30));
    std::string::~string(((char *)arg2 - 0x60));
    std::allocator<char>::~allocator(((char *)arg2 - 0x31));
    std::string::~string(((char *)arg2 - 0x130));
    std::string::~string(((char *)arg2 - 0x110));
    *(int64_t *)((char *)arg2 - 8);
    *(int64_t *)arg2;
    return _Unwind_Resume(arg1);
}

int64_t sub_2677(struct _Unwind_Exception *arg1 @rax, void *arg2 @rbp)
{
    std::string::~string(((char *)arg2 - 0x60));
    std::allocator<char>::~allocator(((char *)arg2 - 0x31));
    std::string::~string(((char *)arg2 - 0x130));
    std::string::~string(((char *)arg2 - 0x110));
    *(int64_t *)((char *)arg2 - 8);
    *(int64_t *)arg2;
    return _Unwind_Resume(arg1);
}

int64_t sub_2688(struct _Unwind_Exception *arg1 @rax, void *arg2 @rbp)
{
    std::allocator<char>::~allocator(((char *)arg2 - 0x31));
    std::string::~string(((char *)arg2 - 0x130));
    std::string::~string(((char *)arg2 - 0x110));
    *(int64_t *)((char *)arg2 - 8);
    *(int64_t *)arg2;
    return _Unwind_Resume(arg1);
}

void __static_initialization_and_destruction_0(int32_t arg1, int32_t arg2)
{
    if ((arg1 == 1 && arg2 == 0xffff))
    {
        std::ios_base::Init::Init(&std::__ioinit);
        __cxa_atexit(std::ios_base::Init::~Init, &std::__ioinit, &__dso_handle);
    }
}

int64_t(static initializer)::magic()
{
    return __static_initialization_and_destruction_0(1, 0xffff);
}

uint64_t std::char_traits<char>::length(char *arg1)
{
    char *var_10 = arg1;
    return strlen(arg1);
}

uint64_t char_traits<char>::eq(char *arg1, char *arg2)
{
    uint64_t rax_2;
    rax_2 = *(int8_t *)arg1 == *(int8_t *)arg2;
    return rax_2;
}

int64_t char_traits<char>::length(void *arg1)
{
    int64_t var_10 = 0;
    while (true)
    {
        char var_11 = 0;
        if ((char_traits<char>::eq(((char *)arg1 + var_10), &var_11) ^ 1) == 0)
        {
            break;
        }
        var_10 = (var_10 + 1);
    }
    return var_10;
}

int64_t std::string::_Alloc_hider::~_Alloc_hider(
    class std::allocator<char> *arg1)
{
    return std::allocator<char>::~allocator(arg1);
}

int64_t std::string::string<std::allocator<char>>(
    struct std::string::_Alloc_hider *arg1, char *arg2)
{
    std::string::_Alloc_hider::_Alloc_hider(arg1, std::string::_M_local_data(arg1));
    void *rax_5;
    if (arg2 == 0)
    {
        rax_5 = &*(int32_t *)nullptr->ident.signature[1];
    }
    else
    {
        rax_5 = &arg2[std::char_traits<char>::length(arg2)];
    }
    return std::string::_M_construct<char const *>(arg1, arg2, rax_5);
}

int64_t std::distance<char const *>(int64_t arg1, int64_t arg2)
{
    return std::__distance<char const *>(arg1, arg2);
}

int64_t std::string::_M_construct<char const *>(class std::string *arg1,
                                                char *arg2, char *arg3)
{
    char rax_1 = __is_null_pointer<char const>(arg2);
    char rax_3;
    if ((rax_1 == 0 || (rax_1 != 0 && arg2 == arg3)))
    {
        rax_3 = 0;
    }
    if ((rax_1 != 0 && arg2 != arg3))
    {
        rax_3 = 1;
    }
    if (rax_3 != 0)
    {
        std::__throw_logic_error("basic_string::_M_construct null …");
    }
    std::string::size_type var_20 = std::distance<char const *>(arg2, arg3);
    if (var_20 > 0xf)
    {
        std::string::_M_data(arg1, std::string::_M_create(arg1, &var_20, 0));
        std::string::_M_capacity(arg1, var_20);
    }
    std::string::_S_copy_chars(std::string::_M_data(arg1), arg2, arg3);
    return std::string::_M_set_length(arg1, var_20);
}

int64_t sub_299d(void *arg1 @rax, void *arg2 @rbp) __noreturn
{
    __cxa_begin_catch(arg1);
    std::string::_M_dispose(*(int64_t *)((char *)arg2 - 0x28));
    __cxa_rethrow();
    /* no return */
}

int64_t __is_null_pointer<char const>(int64_t arg1)
{
    int64_t rax;
    rax = arg1 == 0;
    return rax;
}

int64_t std::__iterator_category<char const *>()
{
    int64_t rdi;
    int64_t var_10 = rdi;
}

int64_t std::__distance<char const *>(int64_t arg1, int64_t arg2)
{
    return (arg2 - arg1);
}

int64_t _fini()
{
    return;
}
