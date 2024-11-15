import ClassRoom from "./0-classroom.mjs";

describe("ClassRoom", () => {
  it("should create a classroom with the correct maxStudentsSize", () => {
    const room = new ClassRoom(10); // Create an instance of ClassRoom
    expect(room._maxStudentsSize).toBe(10); // Check the maxStudentsSize property
  });
});
