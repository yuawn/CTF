int Decode(int arg0) {
    var_18 = arg0;
    var_4 = 0x0;
    do {
            rax = var_4;
            if (rax > 0x1c) {
                break;
            }
            rsi = *(int8_t *)(sign_extend_32(var_4) + 0x601050) & 0xff;
            *(int8_t *)(sign_extend_32(var_4) + 0x601050) = rsi ^ *(int8_t *)(var_18 + sign_extend_64(var_4 - (((SAR(var_4 * 0x2aaaaaab, 0x2)) - (SAR(var_4, 0x1f))) + ((SAR(var_4 * 0x2aaaaaab, 0x2)) - (SAR(var_4, 0x1f))) + ((SAR(var_4 * 0x2aaaaaab, 0x2)) - (SAR(var_4, 0x1f))) << 0x3))) & 0xff;
            var_4 = var_4 + 0x1;
    } while (true);
    return rax;
}
