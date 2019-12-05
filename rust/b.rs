fn main() {
    let v = vec![1, 2, 3];
    let v_ref = &v;
    assert_eq!(v[1], v_ref[1]);
}
