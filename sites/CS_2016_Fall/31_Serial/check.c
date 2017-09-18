int check(int arg0) {
    a = arg0;
    if ((a + 0x10) + (a + 0x8) * (a + 0xc) + (a + 0x4) * a != 0x8e98afe5) {
            rax = 0x0;
    }
    else {
            if ((a + 0x10) + a * (a + 0x8) + (a + 0x4) != 0x9995264b) {
                    rax = 0x0;
            }
            else {
                    if ((a + 0x10) + (a + 0xc) + (a + 0x8) + (a + 0x4) + a != 0x7b707b6f) {
                            rax = 0x0;
                    }
                    else {
                            if (((a + 0xc) + a) * ((a + 0x10) + (a + 0x8) + (a + 0x4)) != 0x80ca1870) {
                                    rax = 0x0;
                            }
                            else {
                                    if ((a + 0x10) + (a + 0x8) + (a + 0x4) != 0xdedde5df) {
                                            rax = 0x0;
                                    }
                                    else {
                                            if ((a + 0x10) * a != 0x1e6b11dc) {
                                                    rax = 0x0;
                                            }
                                            else {
                                                    if ((a + 0x8) * (a + 0x4) != 0x6337562) {
                                                            rax = 0x0;
                                                    }
                                                    else {
                                                            if ((a + 0x10) * (a + 0x4) * (a + 0x8) * (a + 0xc) * (a + 0x8) != 0x1c41db10) {
                                                                    rax = 0x0;
                                                            }
                                                            else {
                                                                    if ((a + 0xc) * (a + 0x8) != 0x83cd7562) {
                                                                            rax = 0x0;
                                                                    }
                                                                    else {
                                                                            rax = 0x1;
                                                                    }
                                                            }
                                                    }
                                            }
                                    }
                            }
                    }
            }
    }
    return rax;
}
