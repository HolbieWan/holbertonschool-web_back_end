export default function createInt8TypedArray(length, position, value) {
  let buffer = new ArrayBuffer(length);
  let dataView = new DataView(buffer);

  if (position >= length || position < 0) {
    throw new Error("Position outside range");
  }

  dataView.setInt8(position, value);
  return dataView;
}
