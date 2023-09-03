# rosbag-processing

## 01_bag-to-csv.py

Usage:
```bash
./01_bag-to-csv.py record.bag
```

Result:
```
record.bag -> [
    ./record/alpha-world.csv,
    ./record/beta-world.csv,
    ./record/gamma-world.csv,
    ./record/n0-range.csv,
    ./record/n1-range.csv,
    ./record/n2-range.csv,
    ./record/n3-range.csv,
    ./record/n4-range.csv,
    ./record/n5-range.csv,
    ./record/n6-range.csv,
    ./record/n7-range.csv,
    ./record/n8-range.csv,
    ./record/n9-range.csv,
    ./record/n10-range.csv,
    ./record/n11-range.csv,
    ./record/n12-range.csv,
    ./record/n13-range.csv,
    ./record/n14-range.csv,
    ./record/n15-range.csv,
    ./record/n16-range.csv,
    ./record/n17-range.csv
]
```

## 02_mocap-csv-to-xyzrpy.py 

Usage:
```bash
./02_mocap-csv-to-xyzrpy.py alpha-world.csv
```

Result:
```
alpha-world.csv -> alpha-world_xyzrpy.csv
```

## 03_uwb-csv-to-range.py

Usage:
```bash
./03_uwb-csv-to-range.py n0-range.csv
```

Result:
```bash
n0-range.csv -> n0-range_uwb.csv
```

## 04_merge-time-nearest.py

Usage:
```bash
./04_merge-time-nearest.py \
    -f alpha-world_xyzrpy.csv -f beta-world_xyzrpy.csv -f gamma-world_xyzrpy.csv \
    -f n0-range_uwb.csv \
    -f n1-range_uwb.csv \
    -f n2-range_uwb.csv \
    -f n3-range_uwb.csv \
    -f n4-range_uwb.csv \
    -f n5-range_uwb.csv \
    -f n6-range_uwb.csv \
    -f n7-range_uwb.csv \
    -f n8-range_uwb.csv \
    -f n9-range_uwb.csv \
    -f n10-range_uwb.csv \
    -f n11-range_uwb.csv \
    -f n12-range_uwb.csv \
    -f n13-range_uwb.csv \
    -f n14-range_uwb.csv \
    -f n15-range_uwb.csv \
    -f n16-range_uwb.csv \
    -f n17-range_uwb.csv \
    -p p1 -p p2 -p p3 \
    -p n0 \
    -p n1 \
    -p n2 \
    -p n3 \
    -p n4 \
    -p n5 \
    -p n6 \
    -p n7 \
    -p n8 \
    -p n9 \
    -p n10 \
    -p n11 \
    -p n12 \
    -p n13 \
    -p n14 \
    -p n15 \
    -p n16 \
    -p n17 \
    -o merge.csv -s 0.04
```

Result:
```bash
# creates merge.csv with the following columns
t merge_t
p1_t p1_x p1_y p1_z p1_roll p1_pitch p1_yaw
p2_t p2_x p2_y p2_z p2_roll p2_pitch p2_yaw
p3_t p3_x p3_y p3_z p3_roll p3_pitch p3_yaw
n0_t n0_n1 n0_n2 n0_n3 n0_n4 n0_n5 n0_n6 n0_n7 n0_n8 n0_n9 n0_n10 n0_n11 n0_n12 n0_n13 n0_n14 n0_n15 n0_n16 n0_n17
n1_t n1_n0 n1_n2 n1_n3 n1_n4 n1_n5 n1_n6 n1_n7 n1_n8 n1_n9 n1_n10 n1_n11 n1_n12 n1_n13 n1_n14 n1_n15 n1_n16 n1_n17
n2_t n2_n0 n2_n1 n2_n3 n2_n4 n2_n5 n2_n6 n2_n7 n2_n8 n2_n9 n2_n10 n2_n11 n2_n12 n2_n13 n2_n14 n2_n15 n2_n16 n2_n17
n3_t n3_n0 n3_n1 n3_n2 n3_n4 n3_n5 n3_n6 n3_n7 n3_n8 n3_n9 n3_n10 n3_n11 n3_n12 n3_n13 n3_n14 n3_n15 n3_n16 n3_n17
n4_t n4_n0 n4_n1 n4_n2 n4_n3 n4_n5 n4_n6 n4_n7 n4_n8 n4_n9 n4_n10 n4_n11 n4_n12 n4_n13 n4_n14 n4_n15 n4_n16 n4_n17
n5_t n5_n0 n5_n1 n5_n2 n5_n3 n5_n4 n5_n6 n5_n7 n5_n8 n5_n9 n5_n10 n5_n11 n5_n12 n5_n13 n5_n14 n5_n15 n5_n16 n5_n17
n6_t n6_n0 n6_n1 n6_n2 n6_n3 n6_n4 n6_n5 n6_n7 n6_n8 n6_n9 n6_n10 n6_n11 n6_n12 n6_n13 n6_n14 n6_n15 n6_n16 n6_n17
n7_t n7_n0 n7_n1 n7_n2 n7_n3 n7_n4 n7_n5 n7_n6 n7_n8 n7_n9 n7_n10 n7_n11 n7_n12 n7_n13 n7_n14 n7_n15 n7_n16 n7_n17
n8_t n8_n0 n8_n1 n8_n2 n8_n3 n8_n4 n8_n5 n8_n6 n8_n7 n8_n9 n8_n10 n8_n11 n8_n12 n8_n13 n8_n14 n8_n15 n8_n16 n8_n17
n9_t n9_n0 n9_n1 n9_n2 n9_n3 n9_n4 n9_n5 n9_n6 n9_n7 n9_n8 n9_n10 n9_n11 n9_n12 n9_n13 n9_n14 n9_n15 n9_n16 n9_n17
n10_t n10_n0 n10_n1 n10_n2 n10_n3 n10_n4 n10_n5 n10_n6 n10_n7 n10_n8 n10_n9 n10_n11 n10_n12 n10_n13 n10_n14 n10_n15 n10_n16 n10_n17
n11_t n11_n0 n11_n1 n11_n2 n11_n3 n11_n4 n11_n5 n11_n6 n11_n7 n11_n8 n11_n9 n11_n10 n11_n12 n11_n13 n11_n14 n11_n15 n11_n16 n11_n17
n12_t n12_n0 n12_n1 n12_n2 n12_n3 n12_n4 n12_n5 n12_n6 n12_n7 n12_n8 n12_n9 n12_n10 n12_n11 n12_n13 n12_n14 n12_n15 n12_n16 n12_n17
n13_t n13_n0 n13_n1 n13_n2 n13_n3 n13_n4 n13_n5 n13_n6 n13_n7 n13_n8 n13_n9 n13_n10 n13_n11 n13_n12 n13_n14 n13_n15 n13_n16 n13_n17
n14_t n14_n0 n14_n1 n14_n2 n14_n3 n14_n4 n14_n5 n14_n6 n14_n7 n14_n8 n14_n9 n14_n10 n14_n11 n14_n12 n14_n13 n14_n15 n14_n16 n14_n17
n15_t n15_n0 n15_n1 n15_n2 n15_n3 n15_n4 n15_n5 n15_n6 n15_n7 n15_n8 n15_n9 n15_n10 n15_n11 n15_n12 n15_n13 n15_n14 n15_n16 n15_n17
n16_t n16_n0 n16_n1 n16_n2 n16_n3 n16_n4 n16_n5 n16_n6 n16_n7 n16_n8 n16_n9 n16_n10 n16_n11 n16_n12 n16_n13 n16_n14 n16_n15 n16_n17
n17_t n17_n0 n17_n1 n17_n2 n17_n3 n17_n4 n17_n5 n17_n6 n17_n7 n17_n8 n17_n9 n17_n10 n17_n11 n17_n12 n17_n13 n17_n14 n17_n15 n17_n16
```

## 05_calc-rel-pose.py

Usage:
```bash
./05_calc-rel-pose.py merge.csv p1_p2_merge.csv p1_ p2_ rel_
```

Result:
```
merge.csv -> p1_p2_merge.csv
```
```
# output has all columns in merge.csv, plus these:
rel_x rel_y rel_z rel_roll rel_pitch rel_yaw
```
