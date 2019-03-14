const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#0a1217", /* black   */
  [1] = "#5A5D60", /* red     */
  [2] = "#A6583F", /* green   */
  [3] = "#C79B53", /* yellow  */
  [4] = "#376C93", /* blue    */
  [5] = "#AA6E8C", /* magenta */
  [6] = "#5896BB", /* cyan    */
  [7] = "#ced0d1", /* white   */

  /* 8 bright colors */
  [8]  = "#909192",  /* black   */
  [9]  = "#5A5D60",  /* red     */
  [10] = "#A6583F", /* green   */
  [11] = "#C79B53", /* yellow  */
  [12] = "#376C93", /* blue    */
  [13] = "#AA6E8C", /* magenta */
  [14] = "#5896BB", /* cyan    */
  [15] = "#ced0d1", /* white   */

  /* special colors */
  [256] = "#0a1217", /* background */
  [257] = "#ced0d1", /* foreground */
  [258] = "#ced0d1",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
