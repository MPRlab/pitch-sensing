int frame_count = 1024;
const uint16_t wave_data[1024] =
{0x7ff, 0x7e8, 0x80c, 0x7c2, 0x818, 0x81c, 0x818, 0x7f9, 0x7de, 0x7e2, 0x828, 0x7fe, 0x81b, 0x812, 0x7b6, 0x7fd, 0x839, 0x962, 0x929, 0x86b, 0x89c, 0xc5e, 0xc19, 0x609, 0x405, 0x62d, 0x74e, 0x924, 0x335, 0x485, 0x7e9, 0x9da, 0x7de, 0x710, 0x7a7, 0x875, 0x83f, 0x8e4, 0x798, 0x8a2, 0x824, 0x7f5, 0x8c1, 0x8a1, 0x723, 0x87a, 0x7a9, 0x848, 0x7f2, 0x82f, 0x76b, 0x806, 0x799, 0x897, 0x82b, 0x772, 0x849, 0x82b, 0x7fa, 0x8ed, 0x874, 0x73f, 0x847, 0x81a, 0x7d5, 0x8ba, 0x8a1, 0x6f6, 0x862, 0x78f, 0x7fd, 0x82a, 0x862, 0x73c, 0x831, 0x7a0, 0x842, 0x829, 0x7b5, 0x7b9, 0x835, 0x7ce, 0x8c2, 0x82c, 0x7a3, 0x824, 0x824, 0x7da, 0x8bd, 0x88e, 0x6fd, 0x84c, 0x7b2, 0x7d7, 0x86b, 0x858, 0x718, 0x822, 0x7ac, 0x805, 0x834, 0x843, 0x777, 0x851, 0x7c0, 0x88c, 0x80e, 0x7d0, 0x7f0, 0x83b, 0x7da, 0x8a8, 0x86d, 0x738, 0x829, 0x7e2, 0x7b0, 0x897, 0x858, 0x70f, 0x809, 0x7b8, 0x7df, 0x833, 0x863, 0x8b0, 0x7f5, 0x76c, 0x9f3, 0xac3, 0x6b2, 0x90f, 0x787, 0x6a3, 0x7f5, 0x8db, 0x6aa, 0x6f3, 0x81b, 0x7e1, 0x7dc, 0x8fb, 0x756, 0x7db, 0x852, 0x80e, 0x7e0, 0x8c5, 0x74e, 0x823, 0x827, 0x887, 0x7bc, 0x864, 0x71f, 0x83c, 0x800, 0x8cb, 0x815, 0x7e6, 0x756, 0x820, 0x7cc, 0x89e, 0x87d, 0x78b, 0x764, 0x828, 0x799, 0x859, 0x8b1, 0x77f, 0x7c4, 0x836, 0x7cf, 0x7ef, 0x8c1, 0x731, 0x809, 0x832, 0x835, 0x7ca, 0x890, 0x73e, 0x815, 0x830, 0x876, 0x7fb, 0x821, 0x72c, 0x80f, 0x7ec, 0x89f, 0x838, 0x7f6, 0x753, 0x813, 0x7b5, 0x888, 0x877, 0x7a9, 0x79b, 0x815, 0x7b7, 0x842, 0x8aa, 0x782, 0x7dd, 0x833, 0x7d6, 0x815, 0x88e, 0x751, 0x7fb, 0x83e, 0x80f, 0x802, 0x878, 0x727, 0x80c, 0x823, 0x848, 0x808, 0x83e, 0x729, 0x7ff, 0x800, 0x85e, 0x844, 0x80a, 0x75e, 0x7fb, 0x7e1, 0x856, 0x861, 0x7e2, 0x794, 0x818, 0x7d0, 0x84d, 0x879, 0x7a6, 0x7d2, 0x824, 0x7e7, 0x825, 0x87b, 0x75d, 0x7f8, 0x821, 0x80e, 0x820, 0x85e, 0x73a, 0x7f6, 0x817, 0x819, 0x835, 0x83d, 0x737, 0x7f5, 0x804, 0x82a, 0x84b, 0x835, 0x74c, 0x805, 0x7e8, 0x828, 0x866, 0x813, 0x78a, 0x814, 0x7f5, 0x818, 0x87c, 0x7d2, 0x7c3, 0x816, 0x805, 0x812, 0x86c, 0x79b, 0x7de, 0x81f, 0x815, 0x81f, 0x852, 0x765, 0x7e0, 0x80a, 0x824, 0x829, 0x84d, 0x745, 0x7ef, 0x7f0, 0x82d, 0x840, 0x843, 0x742, 0x7f2, 0x7df, 0x81e, 0x864, 0x836, 0x76a, 0x7ff, 0x7dd, 0x809, 0x87c, 0x81e, 0x78f, 0x816, 0x7e1, 0x7f9, 0x883, 0x807, 0x7a8, 0x825, 0x7ee, 0x7ed, 0x882, 0x7eb, 0x7bf, 0x82a, 0x800, 0x7e0, 0x87c, 0x7c4, 0x7cc, 0x826, 0x810, 0x7da, 0x87b, 0x7a6, 0x7d2, 0x823, 0x81b, 0x7da, 0x87b, 0x796, 0x7d1, 0x821, 0x81f, 0x7d8, 0x87a, 0x797, 0x7cf, 0x824, 0x815, 0x7d3, 0x87e, 0x7ad, 0x7cb, 0x817, 0x813, 0x7ab, 0x7fb, 0x82e, 0x7f7, 0x809, 0x82b, 0x7a8, 0x808, 0x844, 0x7f1, 0x7ec, 0x81a, 0x7b2, 0x813, 0x833, 0x960, 0x87a, 0x77b, 0x83b, 0xb77, 0x429, 0xb90, 0x7f5, 0x88b, 0x47f, 0x732, 0x72d, 0x57c, 0x7e3, 0x745, 0x661, 0x6e6, 0x7cb, 0x83f, 0x802, 0x86f, 0x748, 0x88a, 0x7b2, 0x8c0, 0x82d, 0x798, 0x843, 0x7f5, 0x815, 0x8dd, 0x88a, 0x741, 0x87e, 0x81c, 0x7e6, 0x8ea, 0x89f, 0x715, 0x88b, 0x7cc, 0x7f0, 0x831, 0x891, 0x6f5, 0x830, 0x77c, 0x841, 0x809, 0x7cf, 0x7db, 0x816, 0x7d8, 0x8ab, 0x837, 0x77b, 0x821, 0x83c, 0x7ce, 0x8e3, 0x878, 0x712, 0x85a, 0x7bf, 0x7e1, 0x85a, 0x8a8, 0x70c, 0x840, 0x79c, 0x7fd, 0x836, 0x802, 0x76c, 0x834, 0x7ba, 0x877, 0x811, 0x7ed, 0x7df, 0x853, 0x7cf, 0x8ba, 0x866, 0x740, 0x83d, 0x7e7, 0x7d4, 0x887, 0x863, 0x706, 0x81c, 0x7b4, 0x7d6, 0x865, 0x851, 0x734, 0x83c, 0x7b2, 0x848, 0x80a, 0x82f, 0x7a3, 0x851, 0x7da, 0x88c, 0x852, 0x872, 0x85c, 0x69a, 0x801, 0xa6e, 0x6c5, 0x765, 0x85c, 0x689, 0x6b4, 0x898, 0x7d3, 0x67b, 0x76d, 0x7e5, 0x79f, 0x7dc, 0x860, 0x72d, 0x86d, 0x801, 0x8ef, 0x82d, 0x7d0, 0x74a, 0x819, 0x7c8, 0x892, 0x8a4, 0x76e, 0x790, 0x83b, 0x7b2, 0x835, 0x8d2, 0x769, 0x7c3, 0x83a, 0x7ef, 0x7d9, 0x8c1, 0x735, 0x821, 0x82d, 0x868, 0x7c5, 0x875, 0x734, 0x820, 0x81a, 0x89f, 0x80b, 0x7f8, 0x73d, 0x814, 0x7d1, 0x8a6, 0x85b, 0x7d0, 0x767, 0x825, 0x79e, 0x871, 0x894, 0x781, 0x7bc, 0x823, 0x7c1, 0x814, 0x8c1, 0x760, 0x7fd, 0x841, 0x7fd, 0x7e9, 0x887, 0x73b, 0x808, 0x83c, 0x83d, 0x7fb, 0x85d, 0x729, 0x810, 0x80d, 0x873, 0x80f, 0x81b, 0x73a, 0x801, 0x7de, 0x87c, 0x85f, 0x7e2, 0x780, 0x807, 0x7c6, 0x856, 0x879, 0x7b0, 0x7b6, 0x824, 0x7ce, 0x840, 0x887, 0x77b, 0x7ec, 0x831, 0x7ee, 0x811, 0x879, 0x737, 0x806, 0x827, 0x825, 0x81b, 0x854, 0x72f, 0x7fa, 0x810, 0x82a, 0x838, 0x82d, 0x744, 0x7fd, 0x7fc, 0x83f, 0x855, 0x81b, 0x770, 0x80b, 0x7de, 0x838, 0x86c, 0x7e3, 0x7b5, 0x81c, 0x7f5, 0x825, 0x87b, 0x798, 0x7df, 0x816, 0x806, 0x822, 0x861, 0x767, 0x7ec, 0x81a, 0x815, 0x831, 0x847, 0x73f, 0x7ea, 0x7ff, 0x822, 0x83f, 0x843, 0x73c, 0x7fc, 0x7e8, 0x81f, 0x85d, 0x832, 0x75e, 0x805, 0x7e8, 0x809, 0x87b, 0x812, 0x795, 0x812, 0x7f3, 0x7fd, 0x87f, 0x7ec, 0x7b8, 0x824, 0x802, 0x7f9, 0x870, 0x7bd, 0x7cb, 0x821, 0x81b, 0x7fb, 0x866, 0x785, 0x7dc, 0x80e, 0x831, 0x803, 0x85a, 0x75a, 0x7de, 0x7fa, 0x83c, 0x81a, 0x855, 0x754, 0x7dd, 0x7ea, 0x83c, 0x82e, 0x84d, 0x75a, 0x7e1, 0x7dc, 0x83a, 0x83c, 0x846, 0x75e, 0x7e9, 0x7d1, 0x83a, 0x848, 0x84c, 0x763, 0x7f0, 0x7c8, 0x83b, 0x848, 0x853, 0x766, 0x7f0, 0x7c9, 0x843, 0x836, 0x85d, 0x761, 0x7e5, 0x7f2, 0x826, 0x7b2, 0x801, 0x83c, 0x809, 0x7e2, 0x7f5, 0x7c3, 0x819, 0x81f, 0x815, 0x800, 0x7cc, 0x7e6, 0x82d, 0x92a, 0x8f2, 0x82f, 0x877, 0xbeb, 0xce0, 0x620, 0xabe, 0x4b4, 0x51c, 0xba9, 0x409, 0x37d, 0x6c4, 0x949, 0x817, 0x748, 0x7c5, 0x8a3, 0x8a5, 0x8e0, 0x7fd, 0x8bc, 0x847, 0x843, 0x8e5, 0x8b9, 0x757, 0x850, 0x7ce, 0x7e7, 0x863, 0x899, 0x716, 0x88b, 0x777, 0x84f, 0x7f8, 0x806, 0x799, 0x814, 0x7d0, 0x89c, 0x848, 0x76a, 0x82d, 0x80d, 0x7e9, 0x8f3, 0x864, 0x74a, 0x868, 0x7f7, 0x7d4, 0x88b, 0x8aa, 0x6d1, 0x855, 0x77d, 0x801, 0x81b, 0x845, 0x76a, 0x81f, 0x7be, 0x861, 0x822, 0x7d0, 0x7dd, 0x84e, 0x7cd, 0x8da, 0x835, 0x755, 0x833, 0x802, 0x7d2, 0x896, 0x8ab, 0x6fd, 0x83d, 0x7a9, 0x7d8, 0x859, 0x840, 0x72d, 0x81f, 0x7ad, 0x832, 0x817, 0x836, 0x78c, 0x85c, 0x7c0, 0x8a2, 0x846, 0x7ae, 0x80f, 0x823, 0x7d2, 0x88d, 0x868, 0x728, 0x815, 0x7d8, 0x7b7, 0x88d, 0x85e, 0x8a2, 0x804, 0x75f, 0x968, 0x9bf, 0x68b, 0x89d, 0x83b, 0x6bc, 0x841, 0x8fa, 0x789, 0x6c0, 0x823, 0x830, 0x7ef, 0x8d0, 0x76c, 0x7a8, 0x840, 0x7d3, 0x81b, 0x8ef, 0x76a, 0x7ce, 0x835, 0x812, 0x7d4, 0x8c1, 0x744, 0x83c, 0x823, 0x897, 0x7c8, 0x866, 0x71e, 0x81e, 0x7fa, 0x8be, 0x827, 0x7d6, 0x75c, 0x81e, 0x7c1, 0x899, 0x881, 0x797, 0x76d, 0x829, 0x79a, 0x850, 0x8b3, 0x777, 0x7d2, 0x833, 0x7da, 0x7ec, 0x8c1, 0x73c, 0x80e, 0x840, 0x835, 0x7d7, 0x876, 0x737, 0x810, 0x82e, 0x871, 0x7fe, 0x82b, 0x72b, 0x815, 0x7ec, 0x897, 0x82d, 0x7ed, 0x751, 0x80b, 0x7bb, 0x87f, 0x87a, 0x7af, 0x7a0, 0x815, 0x7bc, 0x83c, 0x893, 0x782, 0x7d8, 0x834, 0x7d6, 0x820, 0x889, 0x753, 0x800, 0x83b, 0x809, 0x7fc, 0x872, 0x726, 0x80b, 0x823, 0x844, 0x814, 0x840, 0x731, 0x7fc, 0x800, 0x84c, 0x845, 0x810, 0x75e, 0x7ff, 0x7e8, 0x854, 0x861, 0x7ed, 0x794, 0x818, 0x7d3, 0x844, 0x876, 0x7a9, 0x7d4, 0x824, 0x7f2, 0x824, 0x877, 0x763, 0x7f5, 0x81b, 0x80b, 0x823, 0x855, 0x740, 0x7f4, 0x817, 0x817, 0x838, 0x83e, 0x735, 0x7f3, 0x7fd, 0x824, 0x849, 0x838, 0x74d, 0x807, 0x7e9, 0x820, 0x869, 0x815, 0x789, 0x810, 0x7f5, 0x80e, 0x87c, 0x7dd, 0x7c1, 0x819, 0x804, 0x80c, 0x86f, 0x7a7, 0x7d6, 0x820, 0x815, 0x814, 0x858, 0x774, 0x7dd, 0x80b, 0x828, 0x81f, 0x851, 0x74c, 0x7ea, 0x7f1, 0x832, 0x837, 0x846, 0x742, 0x7eb, 0x7de, 0x825, 0x85d, 0x83a, 0x763, 0x7fa, 0x7d8};