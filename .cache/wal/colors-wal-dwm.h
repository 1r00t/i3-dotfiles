static const char norm_fg[] = "#ced0d1";
static const char norm_bg[] = "#0a1217";
static const char norm_border[] = "#909192";

static const char sel_fg[] = "#ced0d1";
static const char sel_bg[] = "#A6583F";
static const char sel_border[] = "#ced0d1";

static const char urg_fg[] = "#ced0d1";
static const char urg_bg[] = "#5A5D60";
static const char urg_border[] = "#5A5D60";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
