int frame_count = 1024;
const uint16_t wave_data[1024] =
{0x7ff, 0x7fb, 0x7f6, 0x6eb, 0x81a, 0x808, 0x7be, 0x82c, 0x7c7, 0x80e, 0x8d2, 0x774, 0x80e, 0x8fa, 0x6fd, 0x817, 0x7e1, 0x7ea, 0x830, 0x7be, 0x813, 0x8f5, 0x755, 0x80b, 0x8cb, 0x70b, 0x811, 0x7d0, 0x800, 0x82a, 0x7bf, 0x815, 0x8f8, 0x74f, 0x808, 0x8b0, 0x719, 0x809, 0x7c7, 0x803, 0x824, 0x7c5, 0x818, 0x8f3, 0x75e, 0x802, 0x8aa, 0x721, 0x801, 0x7c8, 0x7fe, 0x81f, 0x7c7, 0x81b, 0x8e9, 0x771, 0x7ff, 0x8b4, 0x724, 0x7fc, 0x7d2, 0x7ef, 0x817, 0x7c3, 0x81f, 0x8d6, 0x785, 0x802, 0x8c7, 0x725, 0x7f8, 0x7e6, 0x7d8, 0x80e, 0x7b9, 0x81c, 0x8b8, 0x79d, 0x80b, 0x8e1, 0x72b, 0x7f7, 0x809, 0x7ba, 0x802, 0x7ae, 0x811, 0x88c, 0x7b1, 0x814, 0x8f6, 0x73c, 0x7fc, 0x83f, 0x793, 0x7f9, 0x7b3, 0x800, 0x853, 0x7bb, 0x816, 0x8ef, 0x75d, 0x809, 0x87a, 0x76c, 0x7fb, 0x7cf, 0x7ec, 0x824, 0x7bf, 0x80f, 0x8cc, 0x782, 0x811, 0x8a9, 0x751, 0x804, 0x7f8, 0x7d4, 0x808, 0x7c1, 0x808, 0x89a, 0x7a5, 0x80e, 0x8cb, 0x748, 0x80a, 0x821, 0x7b7, 0x800, 0x7c2, 0x804, 0x86b, 0x7bc, 0x809, 0x8d7, 0x751, 0x808, 0x849, 0x797, 0x802, 0x7c6, 0x7ff, 0x843, 0x7ca, 0x809, 0x8d0, 0x76a, 0x803, 0x86e, 0x779, 0x806, 0x7cf, 0x7f0, 0x829, 0x7ce, 0x80d, 0x8b9, 0x78e, 0x800, 0x88c, 0x767, 0x806, 0x7de, 0x7da, 0x81c, 0x7c9, 0x80e, 0x89f, 0x7b0, 0x802, 0x8a2, 0x764, 0x800, 0x7f5, 0x7c3, 0x812, 0x7bf, 0x80a, 0x886, 0x7c6, 0x808, 0x8af, 0x76d, 0x7fc, 0x813, 0x7ae, 0x808, 0x7b8, 0x800, 0x86d, 0x7d2, 0x80e, 0x8b5, 0x77f, 0x7ff, 0x82f, 0x7a2, 0x800, 0x7b5, 0x7f3, 0x857, 0x7d3, 0x80f, 0x8b7, 0x792, 0x803, 0x84a, 0x79c, 0x7fb, 0x7b7, 0x7e7, 0x83f, 0x7cd, 0x80b, 0x8b5, 0x7a3, 0x807, 0x862, 0x79d, 0x7fb, 0x7bd, 0x7e1, 0x82b, 0x7c4, 0x806, 0x8ad, 0x7ae, 0x809, 0x875, 0x79e, 0x7fe, 0x7c6, 0x7de, 0x81b, 0x7bd, 0x802, 0x8a1, 0x7b5, 0x808, 0x881, 0x7a2, 0x802, 0x7cd, 0x7de, 0x815, 0x7b8, 0x800, 0x897, 0x7b8, 0x804, 0x884, 0x7a8, 0x803, 0x7cc, 0x7e4, 0x817, 0x7b7, 0x802, 0x896, 0x7b4, 0x801, 0x877, 0x7b0, 0x802, 0x7bf, 0x7ee, 0x827, 0x7bd, 0x804, 0x89b, 0x7ad, 0x7ff, 0x851, 0x7c0, 0x801, 0x7ad, 0x7fc, 0x847, 0x7c4, 0x802, 0x89e, 0x7a9, 0x7fe, 0x816, 0x7d8, 0x805, 0x7aa, 0x806, 0x86a, 0x7bf, 0x800, 0x88a, 0x7af, 0x7fb, 0x7df, 0x7ee, 0x819, 0x7b7, 0x80a, 0x887, 0x7b4, 0x7fe, 0x859, 0x7c1, 0x7f8, 0x7b8, 0x800, 0x83e, 0x7c3, 0x808, 0x891, 0x7af, 0x7fd, 0x815, 0x7db, 0x7ff, 0x7b1, 0x80b, 0x866, 0x7c1, 0x804, 0x87d, 0x7b6, 0x7f8, 0x7d8, 0x7f2, 0x815, 0x7be, 0x80e, 0x883, 0x7b9, 0x804, 0x84d, 0x7c7, 0x7f5, 0x7b8, 0x800, 0x835, 0x7c8, 0x80c, 0x88b, 0x7b7, 0x803, 0x811, 0x7db, 0x7fb, 0x7b3, 0x808, 0x857, 0x7e4, 0x7fa, 0x821, 0x81a, 0x7f9, 0x80b, 0x7fc, 0x7ef, 0x7fe, 0x80a, 0x800, 0x7f9, 0x805, 0x80c, 0x803, 0x7ff, 0x801, 0x7fe, 0x7fc, 0x7fe, 0x801, 0x7ff, 0x7fe, 0x7fb, 0x7b6, 0x80f, 0x973, 0x6c9, 0x817, 0x905, 0x6d0, 0x828, 0x7ca, 0x806, 0x87e, 0x78a, 0x814, 0x9a0, 0x677, 0x81b, 0x83a, 0x75c, 0x82f, 0x7b1, 0x819, 0x8ee, 0x76b, 0x811, 0x97b, 0x691, 0x817, 0x7d1, 0x7d7, 0x835, 0x7a2, 0x822, 0x947, 0x708, 0x80e, 0x8f1, 0x6d5, 0x80f, 0x7a9, 0x811, 0x852, 0x7b7, 0x81e, 0x972, 0x6da, 0x805, 0x865, 0x746, 0x80e, 0x79a, 0x827, 0x89a, 0x7ad, 0x817, 0x969, 0x6cc, 0x7fa, 0x807, 0x7aa, 0x808, 0x799, 0x82c, 0x8df, 0x775, 0x80c, 0x91d, 0x6e6, 0x7f2, 0x7d6, 0x7e6, 0x819, 0x7bb, 0x827, 0x919, 0x747, 0x800, 0x8bf, 0x72b, 0x7ee, 0x7b8, 0x805, 0x844, 0x7c5, 0x81f, 0x934, 0x720, 0x7f4, 0x86c, 0x778, 0x7e8, 0x7a9, 0x810, 0x879, 0x7b0, 0x814, 0x927, 0x70c, 0x7ef, 0x830, 0x7b6, 0x7ec, 0x7ba, 0x811, 0x8b3, 0x792, 0x80a, 0x8fa, 0x71e, 0x7ed, 0x800, 0x7e2, 0x7ff, 0x7ce, 0x80e, 0x8e3, 0x76e, 0x800, 0x8bc, 0x747, 0x7e9, 0x7d5, 0x7fd, 0x81d, 0x7d4, 0x809, 0x900, 0x746, 0x7f8, 0x880, 0x77b, 0x7e7, 0x7c3, 0x80c, 0x84a, 0x7cf, 0x803, 0x904, 0x72c, 0x7f4, 0x842, 0x7b1, 0x7ed, 0x7ca, 0x812, 0x884, 0x7be, 0x7fa, 0x8e4, 0x734, 0x7ef, 0x7fa, 0x7df, 0x7fe, 0x7d6, 0x812, 0x8ba, 0x798, 0x7f1, 0x8b3, 0x756, 0x7e9, 0x7ca, 0x7fb, 0x81e, 0x7e0, 0x80e, 0x8dc, 0x770, 0x7ea, 0x87b, 0x785, 0x7e9, 0x7b9, 0x809, 0x84b, 0x7e6, 0x806, 0x8df, 0x75c, 0x7e6, 0x832, 0x7b5, 0x7f0, 0x7b9, 0x80f, 0x881, 0x7d5, 0x7fd, 0x8ca, 0x762, 0x7e0, 0x7ee, 0x7d9, 0x801, 0x7c4, 0x80f, 0x8b1, 0x7b3, 0x7f5, 0x8a6, 0x77e, 0x7de, 0x7c3, 0x7f1, 0x81f, 0x7d6, 0x80a, 0x8ca, 0x794, 0x7ef, 0x86e, 0x7a4, 0x7e0, 0x7ad, 0x7ff, 0x848, 0x7dc, 0x802, 0x8cf, 0x784, 0x7ea, 0x82b, 0x7ca, 0x7e7, 0x7a8, 0x805, 0x875, 0x7d1, 0x7fb, 0x8c7, 0x789, 0x7e7, 0x7f3, 0x7e7, 0x7f5, 0x7b4, 0x805, 0x898, 0x7ba, 0x7f4, 0x8ab, 0x79e, 0x7e7, 0x7c7, 0x7fb, 0x80e, 0x7c5, 0x801, 0x8af, 0x7a4, 0x7ee, 0x87b, 0x7bb, 0x7e8, 0x7a9, 0x807, 0x831, 0x7cd, 0x7fc, 0x8bc, 0x796, 0x7ea, 0x844, 0x7dd, 0x7cc, 0x774, 0x817, 0x80b, 0x7e8, 0x80f, 0x828, 0x803, 0x7fc, 0x817, 0x80c, 0x7fd, 0x804, 0x7fd, 0x7f0, 0x7f4, 0x804, 0x802, 0x784, 0x80d, 0x910, 0x6f3, 0x818, 0x7f5, 0x7d6, 0x82f, 0x7c1, 0x810, 0x8e8, 0x761, 0x80d, 0x8e5, 0x704, 0x815, 0x7d7, 0x7f6, 0x831, 0x7bb, 0x813, 0x900, 0x746, 0x80a, 0x8b4, 0x716, 0x80e, 0x7c9, 0x807, 0x82c, 0x7c1, 0x816, 0x8fd, 0x749, 0x805, 0x8a1, 0x721, 0x807, 0x7c4, 0x808, 0x827, 0x7c9, 0x817, 0x8f7, 0x75b, 0x800, 0x89f, 0x728, 0x801, 0x7c6, 0x800, 0x822, 0x7ca, 0x81a, 0x8ea, 0x76f, 0x7fe, 0x8af, 0x72a, 0x7fc, 0x7d1, 0x7ef, 0x819, 0x7c3, 0x81d, 0x8d7, 0x785, 0x803, 0x8c6, 0x72a, 0x7f8, 0x7e8, 0x7d7, 0x80c, 0x7b7, 0x81b, 0x8b5, 0x79e, 0x80e, 0x8e2, 0x72d, 0x7f7, 0x80e, 0x7b6, 0x800, 0x7ae, 0x80f, 0x885, 0x7b4, 0x816, 0x8f5, 0x740, 0x7fe, 0x846, 0x78e, 0x7f9, 0x7b6, 0x7fd, 0x84d, 0x7bd, 0x815, 0x8eb, 0x761, 0x809, 0x87e, 0x76a, 0x7fc, 0x7d4, 0x7eb, 0x821, 0x7bf, 0x80d, 0x8c6, 0x785, 0x810, 0x8ad, 0x750, 0x805, 0x7fe, 0x7d2, 0x806, 0x7c1, 0x807, 0x893, 0x7a8, 0x80d, 0x8cc, 0x749, 0x80b, 0x825, 0x7b5, 0x800, 0x7c3, 0x803, 0x867, 0x7bf, 0x809, 0x8d6, 0x754, 0x808, 0x84b, 0x794, 0x803, 0x7c5, 0x7fe, 0x841, 0x7cc, 0x80a, 0x8ce, 0x76f, 0x801, 0x870, 0x777, 0x805, 0x7ce, 0x7ef, 0x82a, 0x7cf, 0x80e, 0x8b8, 0x791, 0x7ff, 0x88d, 0x766, 0x804, 0x7df, 0x7d8, 0x81c, 0x7c9, 0x80e, 0x89d, 0x7b2, 0x802, 0x8a1, 0x765, 0x800, 0x7f6, 0x7c1, 0x812, 0x7be, 0x809, 0x885, 0x7c7, 0x809, 0x8ae, 0x771, 0x7fd, 0x813, 0x7af, 0x807, 0x7b6, 0x7fe, 0x86d, 0x7d1, 0x80f, 0x8b5, 0x782, 0x7ff, 0x82f, 0x7a3, 0x7fe, 0x7b3, 0x7f2, 0x856, 0x7d2, 0x810, 0x8b7, 0x794, 0x804, 0x84a, 0x79d, 0x7fa, 0x7b6, 0x7e7, 0x83f, 0x7cd, 0x80b, 0x8b4, 0x7a3, 0x807, 0x85f, 0x79e, 0x7fb, 0x7bc, 0x7e2, 0x82c, 0x7c5, 0x806, 0x8ac, 0x7ae, 0x807, 0x872, 0x7a1, 0x7ff, 0x7c4, 0x7e1, 0x81d, 0x7bd, 0x802, 0x8a1, 0x7b3, 0x806, 0x87e, 0x7a5, 0x802, 0x7ca, 0x7e2, 0x818, 0x7b9, 0x801, 0x898, 0x7b5, 0x803, 0x87d, 0x7ab, 0x804, 0x7c6, 0x7e7, 0x81d, 0x7ba, 0x801, 0x899, 0x7b1, 0x801, 0x86a, 0x7b7, 0x802, 0x7b6, 0x7f3, 0x831, 0x7bf, 0x803, 0x89f, 0x7aa, 0x7ff, 0x83e, 0x7c9, 0x801, 0x7a9, 0x800, 0x853, 0x7c3, 0x802, 0x89a, 0x7a9, 0x7ff, 0x802, 0x7df, 0x80a, 0x7ad, 0x807, 0x875, 0x7bc, 0x7ff, 0x87d, 0x7b5, 0x7fb, 0x7cd, 0x7f5, 0x824, 0x7bb, 0x80a, 0x88e, 0x7b1, 0x7fd, 0x844, 0x7ca, 0x7f8, 0x7b1, 0x805, 0x84c, 0x7c4, 0x807, 0x88f, 0x7b0, 0x7fc, 0x7fe, 0x7e3, 0x805, 0x7b5, 0x80b, 0x872, 0x7bf, 0x804, 0x86f, 0x7bc, 0x7f6, 0x7c9, 0x7f7, 0x820, 0x7c1, 0x80e, 0x889, 0x7b8, 0x804, 0x839, 0x7ce, 0x7f5, 0x7b3, 0x804, 0x841, 0x7c9, 0x80c, 0x889, 0x7b8, 0x802, 0x7fc, 0x7e1, 0x7ff, 0x7be, 0x7ef, 0x815, 0x80f, 0x804, 0x817, 0x806, 0x7fd, 0x80c, 0x802, 0x7f3, 0x7fc, 0x807, 0x804, 0x7fc, 0x802, 0x806};
